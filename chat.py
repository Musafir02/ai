import torch
import torch.nn.functional as F
from tokenizer import BPETokenizer
from model import GPTModel

class ChatBot:
    def __init__(self, model_path="gpt_best.pt", tokenizer_path="tokenizer.pkl", device=None):
        self.device = device or torch.device("cuda" if torch.cuda.is_available() else "cpu")
        
        print(f"Loading tokenizer...")
        self.tokenizer = BPETokenizer.load(tokenizer_path)
        
        print(f"Loading model...")
        checkpoint = torch.load(model_path, map_location=self.device, weights_only=False)
        config = checkpoint["config"]
        
        self.model = GPTModel(
            vocab_size=config["vocab_size"],
            d_model=config["d_model"],
            num_heads=config["num_heads"],
            num_layers=config["num_layers"],
            d_ff=config["d_ff"],
            max_len=config["max_len"],
            pad_idx=self.tokenizer.token_to_id["<pad>"]
        ).to(self.device)
        
        self.model.load_state_dict(checkpoint["model_state_dict"])
        self.model.eval()
        
        print(f"Model loaded (epoch {checkpoint['epoch'] + 1}, val_loss: {checkpoint['val_loss']:.4f})")
    
    def chat(self, user_input, max_tokens=100, temperature=0.7, top_k=40, top_p=0.9, verbose=False):
        self.model.eval()
        
        user_ids = [self.tokenizer.token_to_id["<user>"]] + self.tokenizer.encode(user_input)
        start_ids = user_ids + [self.tokenizer.token_to_id["<bot>"]]
        
        if verbose:
            print(f"\n--- Generation Process ---")
            print(f"Input tokens: {len(start_ids)}")
        
        start_tensor = torch.tensor([start_ids], dtype=torch.long).to(self.device)
        
        output = self.model.generate(
            start_tensor,
            max_new_tokens=max_tokens,
            temperature=temperature,
            top_k=top_k,
            top_p=top_p,
            eos_id=self.tokenizer.token_to_id["<eos>"]
        )
        
        output_ids = output[0].tolist()
        
        if verbose:
            print(f"Output tokens: {len(output_ids)}")
            print(f"Temperature: {temperature}")
            print(f"Top-k: {top_k}, Top-p: {top_p}")
            print(f"--- End Process ---\n")
        
        bot_idx = None
        for i, tok_id in enumerate(output_ids):
            if tok_id == self.tokenizer.token_to_id["<bot>"]:
                bot_idx = i
        
        if bot_idx is not None:
            response_ids = output_ids[bot_idx + 1:]
            response_ids = [t for t in response_ids if t not in [
                self.tokenizer.token_to_id["<eos>"],
                self.tokenizer.token_to_id["<pad>"]
            ]]
            return self.tokenizer.decode(response_ids)
        
        return self.tokenizer.decode(output_ids)
    
    def show_attention(self, user_input, layer=0):
        self.model.eval()
        
        user_ids = [self.tokenizer.token_to_id["<user>"]] + self.tokenizer.encode(user_input)
        input_tensor = torch.tensor([user_ids], dtype=torch.long).to(self.device)
        
        with torch.no_grad():
            _ = self.model(input_tensor)
            attention = self.model.get_attention_scores(layer)
        
        if attention is not None:
            print(f"\nAttention Scores (Layer {layer}):")
            print(f"Shape: {attention.shape}")
            print(f"[batch={attention.shape[0]}, heads={attention.shape[1]}, seq={attention.shape[2]}, seq={attention.shape[3]}]")
            
            avg_attention = attention[0].mean(dim=0)
            print(f"\nAverage attention (across {attention.shape[1]} heads):")
            
            tokens = ["<user>"] + [self.tokenizer.id_to_token.get(i, "?") for i in self.tokenizer.encode(user_input)]
            
            for i, token in enumerate(tokens[:min(5, len(tokens))]):
                weights = avg_attention[i][:len(tokens)].tolist()
                weights_str = " ".join([f"{w:.2f}" for w in weights[:min(5, len(weights))]])
                print(f"  {token:15s} -> [{weights_str}...]")
    
    def explain_generation(self, user_input):
        self.model.eval()
        
        print("\n" + "=" * 60)
        print("HOW YOUR AI GENERATES A RESPONSE")
        print("=" * 60)
        
        print("\n1. TOKENIZATION")
        print(f"   Input: '{user_input}'")
        tokens = self.tokenizer.encode(user_input)
        token_names = [self.tokenizer.id_to_token.get(t, "?") for t in tokens]
        print(f"   Tokens: {token_names}")
        print(f"   Token IDs: {tokens}")
        
        user_ids = [self.tokenizer.token_to_id["<user>"]] + tokens + [self.tokenizer.token_to_id["<bot>"]]
        input_tensor = torch.tensor([user_ids], dtype=torch.long).to(self.device)
        
        print("\n2. EMBEDDINGS")
        embeddings = self.model.token_embedding(input_tensor)
        print(f"   Each token -> {embeddings.shape[-1]}-dimensional vector")
        print(f"   Shape: {embeddings.shape}")
        
        print("\n3. POSITIONAL ENCODING")
        pos_emb = self.model.position_encoding(embeddings)
        print(f"   Position information added")
        print(f"   Shape: {pos_emb.shape}")
        
        print("\n4. TRANSFORMER LAYERS")
        with torch.no_grad():
            logits = self.model(input_tensor)
        print(f"   Passed through {len(self.model.layers)} layers")
        print(f"   Each layer: Attention -> FFN")
        
        print("\n5. ATTENTION (what the model 'focuses' on)")
        attention = self.model.get_attention_scores(0)
        if attention is not None:
            print(f"   {attention.shape[1]} attention heads analyze relationships")
        
        print("\n6. LOGITS (raw prediction scores)")
        last_logits = logits[0, -1, :]
        print(f"   Shape: {last_logits.shape} (one score per vocabulary word)")
        print(f"   Range: [{last_logits.min():.2f}, {last_logits.max():.2f}]")
        
        print("\n7. TEMPERATURE SCALING")
        temperature = 0.7
        scaled = last_logits / temperature
        print(f"   Temperature = {temperature}")
        print(f"   Higher T = more random, Lower T = more focused")
        
        print("\n8. SOFTMAX -> PROBABILITIES")
        probs = F.softmax(scaled, dim=-1)
        top_probs, top_ids = probs.topk(5)
        print(f"   Top 5 predictions:")
        for prob, idx in zip(top_probs.tolist(), top_ids.tolist()):
            token = self.tokenizer.id_to_token.get(idx, "?")
            print(f"     '{token}': {prob*100:.2f}%")
        
        print("\n9. SAMPLING")
        print(f"   Model samples from probability distribution")
        print(f"   Top-k and Top-p filter unlikely options")
        
        print("\n10. REPEAT until <eos> or max length")
        print("=" * 60)
        
        response = self.chat(user_input, verbose=False)
        print(f"\nFINAL RESPONSE: {response}")
        print("=" * 60)

def main():
    print("=" * 60)
    print("GPT CHATBOT - With Explicit Components")
    print("=" * 60)
    
    try:
        bot = ChatBot("gpt_best.pt", "tokenizer.pkl")
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("Train the model first with: python train.py")
        return
    
    print("\n" + "=" * 60)
    print("Commands:")
    print("  'quit'     - Exit")
    print("  'explain'  - Show how generation works")
    print("  'attention'- Show attention scores")
    print("=" * 60)
    
    while True:
        try:
            user_input = input("\nYou: ").strip()
            
            if user_input.lower() in ["quit", "exit", "q"]:
                print("Goodbye!")
                break
            
            if not user_input:
                continue
            
            if user_input.lower() == "explain":
                test_input = input("Enter text to explain: ").strip()
                if test_input:
                    bot.explain_generation(test_input)
                continue
            
            if user_input.lower() == "attention":
                test_input = input("Enter text for attention: ").strip()
                if test_input:
                    bot.show_attention(test_input)
                continue
            
            response = bot.chat(user_input)
            print(f"Bot: {response}")
            
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()
