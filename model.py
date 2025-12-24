import torch
import torch.nn as nn
import torch.nn.functional as F
import math

class TokenEmbedding(nn.Module):
    def __init__(self, vocab_size, d_model, pad_idx=0):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, d_model, padding_idx=pad_idx)
        self.d_model = d_model
    
    def forward(self, x):
        return self.embedding(x) * math.sqrt(self.d_model)

class PositionalEncoding(nn.Module):
    def __init__(self, d_model, max_len=512, dropout=0.1):
        super().__init__()
        self.dropout = nn.Dropout(p=dropout)
        
        pe = torch.zeros(max_len, d_model)
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))
        
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        pe = pe.unsqueeze(0)
        
        self.register_buffer('pe', pe)
    
    def forward(self, x):
        x = x + self.pe[:, :x.size(1), :]
        return self.dropout(x)

class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads, dropout=0.1):
        super().__init__()
        assert d_model % num_heads == 0
        
        self.d_model = d_model
        self.num_heads = num_heads
        self.head_dim = d_model // num_heads
        
        self.W_q = nn.Linear(d_model, d_model)
        self.W_k = nn.Linear(d_model, d_model)
        self.W_v = nn.Linear(d_model, d_model)
        self.W_o = nn.Linear(d_model, d_model)
        
        self.dropout = nn.Dropout(dropout)
        self.attention_scores = None
    
    def forward(self, x, mask=None):
        batch_size, seq_len, _ = x.size()
        
        Q = self.W_q(x)
        K = self.W_k(x)
        V = self.W_v(x)
        
        Q = Q.view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
        K = K.view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
        V = V.view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
        
        scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(self.head_dim)
        
        if mask is not None:
            scores = scores.masked_fill(mask == float('-inf'), float('-inf'))
        
        attention_weights = F.softmax(scores, dim=-1)
        self.attention_scores = attention_weights.detach()
        
        attention_weights = self.dropout(attention_weights)
        
        context = torch.matmul(attention_weights, V)
        
        context = context.transpose(1, 2).contiguous().view(batch_size, seq_len, self.d_model)
        
        output = self.W_o(context)
        return output

class FeedForwardNetwork(nn.Module):
    def __init__(self, d_model, d_ff, dropout=0.1):
        super().__init__()
        self.linear1 = nn.Linear(d_model, d_ff)
        self.linear2 = nn.Linear(d_ff, d_model)
        self.dropout = nn.Dropout(dropout)
        self.activation = nn.GELU()
    
    def forward(self, x):
        x = self.linear1(x)
        x = self.activation(x)
        x = self.dropout(x)
        x = self.linear2(x)
        return x

class TransformerBlock(nn.Module):
    def __init__(self, d_model, num_heads, d_ff, dropout=0.1):
        super().__init__()
        
        self.attention = MultiHeadAttention(d_model, num_heads, dropout)
        self.ffn = FeedForwardNetwork(d_model, d_ff, dropout)
        
        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)
        
        self.dropout1 = nn.Dropout(dropout)
        self.dropout2 = nn.Dropout(dropout)
    
    def forward(self, x, mask=None):
        attn_output = self.attention(self.norm1(x), mask)
        x = x + self.dropout1(attn_output)
        
        ffn_output = self.ffn(self.norm2(x))
        x = x + self.dropout2(ffn_output)
        
        return x

class GPTModel(nn.Module):
    def __init__(self, vocab_size, d_model=256, num_heads=8, num_layers=6,
                 d_ff=1024, dropout=0.1, max_len=512, pad_idx=0):
        super().__init__()
        
        self.vocab_size = vocab_size
        self.d_model = d_model
        self.pad_idx = pad_idx
        
        self.token_embedding = TokenEmbedding(vocab_size, d_model, pad_idx)
        self.position_encoding = PositionalEncoding(d_model, max_len, dropout)
        
        self.layers = nn.ModuleList([
            TransformerBlock(d_model, num_heads, d_ff, dropout)
            for _ in range(num_layers)
        ])
        
        self.final_norm = nn.LayerNorm(d_model)
        
        self.output_projection = nn.Linear(d_model, vocab_size)
        
        self._init_weights()
    
    def _init_weights(self):
        for p in self.parameters():
            if p.dim() > 1:
                nn.init.xavier_uniform_(p)
    
    def create_causal_mask(self, seq_len, device):
        mask = torch.triu(torch.ones(seq_len, seq_len, device=device), diagonal=1)
        mask = mask.masked_fill(mask == 1, float('-inf'))
        return mask
    
    def forward(self, input_ids, return_hidden=False):
        batch_size, seq_len = input_ids.size()
        device = input_ids.device
        
        causal_mask = self.create_causal_mask(seq_len, device)
        
        embeddings = self.token_embedding(input_ids)
        
        hidden_states = self.position_encoding(embeddings)
        
        for layer in self.layers:
            hidden_states = layer(hidden_states, causal_mask)
        
        hidden_states = self.final_norm(hidden_states)
        
        logits = self.output_projection(hidden_states)
        
        if return_hidden:
            return logits, hidden_states
        return logits
    
    def get_attention_scores(self, layer_idx=0):
        if layer_idx < len(self.layers):
            return self.layers[layer_idx].attention.attention_scores
        return None
    
    @torch.no_grad()
    def generate(self, start_tokens, max_new_tokens=50, temperature=0.8, 
                 top_k=40, top_p=0.9, eos_id=2):
        self.eval()
        
        generated = start_tokens.clone()
        
        for _ in range(max_new_tokens):
            logits = self.forward(generated)
            
            next_token_logits = logits[:, -1, :]
            
            next_token_logits = next_token_logits / temperature
            
            if top_k > 0:
                top_k_values, _ = torch.topk(next_token_logits, top_k)
                min_top_k = top_k_values[:, -1].unsqueeze(-1)
                next_token_logits = torch.where(
                    next_token_logits < min_top_k,
                    torch.full_like(next_token_logits, float('-inf')),
                    next_token_logits
                )
            
            if top_p < 1.0:
                sorted_logits, sorted_indices = torch.sort(next_token_logits, descending=True)
                cumulative_probs = torch.cumsum(F.softmax(sorted_logits, dim=-1), dim=-1)
                
                sorted_indices_to_remove = cumulative_probs > top_p
                sorted_indices_to_remove[:, 1:] = sorted_indices_to_remove[:, :-1].clone()
                sorted_indices_to_remove[:, 0] = False
                
                indices_to_remove = sorted_indices_to_remove.scatter(
                    1, sorted_indices, sorted_indices_to_remove
                )
                next_token_logits = next_token_logits.masked_fill(indices_to_remove, float('-inf'))
            
            probabilities = F.softmax(next_token_logits, dim=-1)
            
            next_token = torch.multinomial(probabilities, num_samples=1)
            
            generated = torch.cat([generated, next_token], dim=1)
            
            if next_token.item() == eos_id:
                break
        
        return generated

def count_params(model):
    return sum(p.numel() for p in model.parameters() if p.requires_grad)

def test_model():
    print("=== Testing GPT Model Components ===\n")
    
    vocab_size = 1000
    d_model = 256
    num_heads = 8
    num_layers = 6
    
    model = GPTModel(
        vocab_size=vocab_size,
        d_model=d_model,
        num_heads=num_heads,
        num_layers=num_layers
    )
    
    print(f"Model Parameters: {count_params(model):,}")
    
    input_ids = torch.randint(0, vocab_size, (1, 10))
    print(f"\n1. INPUT TOKENS: {input_ids.shape}")
    print(f"   Sample: {input_ids[0].tolist()}")
    
    embeddings = model.token_embedding(input_ids)
    print(f"\n2. TOKEN EMBEDDINGS: {embeddings.shape}")
    print(f"   Each token becomes a {d_model}-dimensional vector")
    
    pos_embeddings = model.position_encoding(embeddings)
    print(f"\n3. + POSITIONAL ENCODING: {pos_embeddings.shape}")
    print(f"   Position information added to embeddings")
    
    logits, hidden = model(input_ids, return_hidden=True)
    print(f"\n4. AFTER {num_layers} TRANSFORMER BLOCKS:")
    print(f"   Hidden States: {hidden.shape}")
    
    attention_scores = model.get_attention_scores(layer_idx=0)
    if attention_scores is not None:
        print(f"\n5. ATTENTION SCORES (Layer 0): {attention_scores.shape}")
        print(f"   Shape: [batch, heads, seq_len, seq_len]")
        print(f"   {num_heads} attention heads each attending to all positions")
    
    print(f"\n6. LOGITS (Raw Scores): {logits.shape}")
    print(f"   Shape: [batch, seq_len, vocab_size]")
    print(f"   Each position has {vocab_size} scores for next token")
    
    last_logits = logits[0, -1, :]
    print(f"\n7. LAST POSITION LOGITS: {last_logits.shape}")
    print(f"   Min: {last_logits.min():.3f}, Max: {last_logits.max():.3f}")
    
    temperature = 0.8
    scaled_logits = last_logits / temperature
    print(f"\n8. TEMPERATURE SCALING (T={temperature}):")
    print(f"   Before: range [{last_logits.min():.3f}, {last_logits.max():.3f}]")
    print(f"   After:  range [{scaled_logits.min():.3f}, {scaled_logits.max():.3f}]")
    
    probabilities = F.softmax(scaled_logits, dim=-1)
    print(f"\n9. SOFTMAX -> PROBABILITIES: {probabilities.shape}")
    print(f"   Sum: {probabilities.sum():.4f} (should be ~1.0)")
    print(f"   Top 5 probs: {probabilities.topk(5).values.tolist()}")
    
    sampled_token = torch.multinomial(probabilities, num_samples=1)
    print(f"\n10. SAMPLED TOKEN: {sampled_token.item()}")
    print(f"    Probability of selected token: {probabilities[sampled_token].item():.4f}")
    
    print("\n" + "=" * 50)
    print("This is exactly how ChatGPT works!")
    print("=" * 50)

if __name__ == "__main__":
    test_model()
