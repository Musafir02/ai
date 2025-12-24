import re
import json
import pickle
from collections import Counter

class BPETokenizer:
    def __init__(self, vocab_size=5000):
        self.vocab_size = vocab_size
        self.special_tokens = {
            "<pad>": 0,
            "<sos>": 1, 
            "<eos>": 2,
            "<unk>": 3,
            "<user>": 4,
            "<bot>": 5,
        }
        self.merges = {}
        self.vocab = {}
        self.token_to_id = {}
        self.id_to_token = {}
    
    def __len__(self):
        return len(self.token_to_id)
    
    def _get_stats(self, words):
        pairs = Counter()
        for word, freq in words.items():
            symbols = word.split()
            for i in range(len(symbols) - 1):
                pairs[(symbols[i], symbols[i+1])] += freq
        return pairs
    
    def _merge_vocab(self, pair, words):
        new_words = {}
        bigram = re.escape(' '.join(pair))
        pattern = re.compile(r'(?<!\S)' + bigram + r'(?!\S)')
        
        for word in words:
            new_word = pattern.sub(''.join(pair), word)
            new_words[new_word] = words[word]
        return new_words
    
    def _preprocess(self, text):
        text = text.lower().strip()
        text = re.sub(r'([.,!?"\'])', r' \1', text)
        text = re.sub(r'\s+', ' ', text)
        return text.strip()
    
    def _tokenize_word(self, word):
        word = ' '.join(list(word)) + ' </w>'
        return word
    
    def train(self, texts):
        print("Training BPE tokenizer...")
        
        word_freq = Counter()
        for text in texts:
            text = self._preprocess(text)
            for word in text.split():
                word_freq[self._tokenize_word(word)] += 1
        
        words = dict(word_freq)
        
        print(f"Initial vocabulary: {len(set(' '.join(words.keys()).split()))} characters")
        
        num_merges = self.vocab_size - len(self.special_tokens) - len(set(' '.join(words.keys()).split()))
        
        for i in range(num_merges):
            pairs = self._get_stats(words)
            if not pairs:
                break
            
            best_pair = max(pairs, key=pairs.get)
            words = self._merge_vocab(best_pair, words)
            self.merges[best_pair] = i
            
            if (i + 1) % 500 == 0:
                print(f"Completed {i + 1} merges...")
        
        vocab = set()
        for word in words:
            for token in word.split():
                vocab.add(token)
        
        self.token_to_id = dict(self.special_tokens)
        self.id_to_token = {v: k for k, v in self.special_tokens.items()}
        
        idx = len(self.special_tokens)
        for token in sorted(vocab):
            if token not in self.token_to_id:
                self.token_to_id[token] = idx
                self.id_to_token[idx] = token
                idx += 1
        
        print(f"Final vocabulary size: {len(self.token_to_id)}")
    
    def _apply_bpe(self, word):
        word = list(word)
        word = [c for c in word] + ['</w>']
        
        while len(word) > 1:
            pairs = [(word[i], word[i+1]) for i in range(len(word) - 1)]
            
            valid_pairs = [(p, self.merges[p]) for p in pairs if p in self.merges]
            
            if not valid_pairs:
                break
            
            best_pair = min(valid_pairs, key=lambda x: x[1])[0]
            
            new_word = []
            i = 0
            while i < len(word):
                if i < len(word) - 1 and (word[i], word[i+1]) == best_pair:
                    new_word.append(word[i] + word[i+1])
                    i += 2
                else:
                    new_word.append(word[i])
                    i += 1
            word = new_word
        
        return word
    
    def encode(self, text):
        text = self._preprocess(text)
        tokens = []
        
        for word in text.split():
            word_tokens = self._apply_bpe(word)
            for token in word_tokens:
                tokens.append(self.token_to_id.get(token, self.token_to_id["<unk>"]))
        
        return tokens
    
    def decode(self, ids, skip_special=True):
        special_ids = set(self.special_tokens.values())
        tokens = []
        
        for idx in ids:
            if skip_special and idx in special_ids:
                continue
            if idx in self.id_to_token:
                tokens.append(self.id_to_token[idx])
        
        text = ''.join(tokens)
        text = text.replace('</w>', ' ')
        text = re.sub(r'\s+', ' ', text).strip()
        return text
    
    def decode_with_special(self, ids):
        tokens = [self.id_to_token.get(idx, "<unk>") for idx in ids]
        return ' '.join(tokens)
    
    def create_sequence(self, user_input, bot_response, max_len=256):
        user_ids = [self.token_to_id["<user>"]] + self.encode(user_input)
        bot_ids = [self.token_to_id["<bot>"]] + self.encode(bot_response) + [self.token_to_id["<eos>"]]
        
        full_seq = user_ids + bot_ids
        
        if len(full_seq) > max_len:
            full_seq = full_seq[:max_len-1] + [self.token_to_id["<eos>"]]
        
        return full_seq
    
    def save(self, path):
        with open(path, "wb") as f:
            pickle.dump({
                "merges": self.merges,
                "token_to_id": self.token_to_id,
                "id_to_token": self.id_to_token,
                "special_tokens": self.special_tokens,
                "vocab_size": self.vocab_size
            }, f)
        print(f"Tokenizer saved to {path}")
    
    @classmethod
    def load(cls, path):
        with open(path, "rb") as f:
            data = pickle.load(f)
        
        tokenizer = cls()
        tokenizer.merges = data["merges"]
        tokenizer.token_to_id = data["token_to_id"]
        tokenizer.id_to_token = data["id_to_token"]
        tokenizer.special_tokens = data["special_tokens"]
        tokenizer.vocab_size = data["vocab_size"]
        return tokenizer

def main():
    with open("train_pairs.json", "r", encoding="utf-8") as f:
        train_pairs = json.load(f)
    
    print(f"Loaded {len(train_pairs)} training pairs")
    
    all_texts = [p["input"] for p in train_pairs] + [p["output"] for p in train_pairs]
    
    tokenizer = BPETokenizer(vocab_size=3000)
    tokenizer.train(all_texts)
    tokenizer.save("tokenizer.pkl")
    
    print("\n=== Test ===")
    test_text = "hello how are you doing today"
    encoded = tokenizer.encode(test_text)
    decoded = tokenizer.decode(encoded)
    print(f"Original: {test_text}")
    print(f"Encoded: {encoded}")
    print(f"Decoded: {decoded}")
    
    print("\n=== Unknown word test ===")
    test_text = "supercalifragilistic"
    encoded = tokenizer.encode(test_text)
    decoded = tokenizer.decode(encoded)
    print(f"Original: {test_text}")
    print(f"Tokens: {[tokenizer.id_to_token[i] for i in encoded]}")
    print(f"Decoded: {decoded}")

if __name__ == "__main__":
    main()
