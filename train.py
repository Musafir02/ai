import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import json
from tqdm import tqdm

from tokenizer import BPETokenizer
from model import GPTModel, count_params

class ChatDataset(Dataset):
    def __init__(self, pairs_path, tokenizer, max_len=256):
        with open(pairs_path, "r", encoding="utf-8") as f:
            self.pairs = json.load(f)
        self.tokenizer = tokenizer
        self.max_len = max_len
    
    def __len__(self):
        return len(self.pairs)
    
    def __getitem__(self, idx):
        pair = self.pairs[idx]
        seq = self.tokenizer.create_sequence(
            pair["input"], 
            pair["output"], 
            max_len=self.max_len
        )
        
        if len(seq) < self.max_len:
            seq = seq + [self.tokenizer.token_to_id["<pad>"]] * (self.max_len - len(seq))
        
        input_ids = seq[:-1]
        labels = seq[1:]
        
        return {
            "input_ids": torch.tensor(input_ids, dtype=torch.long),
            "labels": torch.tensor(labels, dtype=torch.long)
        }

def train_epoch(model, loader, optimizer, criterion, device, clip=1.0):
    model.train()
    total_loss = 0
    
    pbar = tqdm(loader, desc="Training")
    for batch in pbar:
        input_ids = batch["input_ids"].to(device)
        labels = batch["labels"].to(device)
        
        optimizer.zero_grad()
        
        logits = model(input_ids)
        
        logits = logits.reshape(-1, logits.size(-1))
        labels = labels.reshape(-1)
        
        loss = criterion(logits, labels)
        loss.backward()
        
        torch.nn.utils.clip_grad_norm_(model.parameters(), clip)
        optimizer.step()
        
        total_loss += loss.item()
        pbar.set_postfix({"loss": f"{loss.item():.4f}"})
    
    return total_loss / len(loader)

def evaluate(model, loader, criterion, device):
    model.eval()
    total_loss = 0
    
    with torch.no_grad():
        for batch in tqdm(loader, desc="Evaluating"):
            input_ids = batch["input_ids"].to(device)
            labels = batch["labels"].to(device)
            
            logits = model(input_ids)
            logits = logits.reshape(-1, logits.size(-1))
            labels = labels.reshape(-1)
            
            loss = criterion(logits, labels)
            total_loss += loss.item()
    
    return total_loss / len(loader)

def main():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Device: {device}")
    
    BATCH_SIZE = 32
    MAX_LEN = 256
    D_MODEL = 256
    NUM_HEADS = 8
    NUM_LAYERS = 6
    D_FF = 1024
    DROPOUT = 0.1
    LR = 0.0003
    EPOCHS = 50
    
    print("\n=== Creating Dataset ===")
    import create_dataset
    create_dataset.create_dataset()
    
    print("\n=== Training BPE Tokenizer ===")
    with open("train_pairs.json", "r", encoding="utf-8") as f:
        train_pairs = json.load(f)
    
    all_texts = [p["input"] for p in train_pairs] + [p["output"] for p in train_pairs]
    
    tokenizer = BPETokenizer(vocab_size=3000)
    tokenizer.train(all_texts)
    tokenizer.save("tokenizer.pkl")
    
    print("\n=== Loading Data ===")
    train_dataset = ChatDataset("train_pairs.json", tokenizer, MAX_LEN)
    val_dataset = ChatDataset("val_pairs.json", tokenizer, MAX_LEN)
    
    train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True, num_workers=0)
    val_loader = DataLoader(val_dataset, batch_size=BATCH_SIZE, shuffle=False, num_workers=0)
    
    print(f"Train: {len(train_dataset)}, Val: {len(val_dataset)}")
    
    print("\n=== Creating GPT Model ===")
    print(f"Architecture:")
    print(f"  - Token Embedding: vocab_size={len(tokenizer)} -> d_model={D_MODEL}")
    print(f"  - Positional Encoding: max_len={MAX_LEN}")
    print(f"  - Transformer Blocks: {NUM_LAYERS} layers")
    print(f"  - Multi-Head Attention: {NUM_HEADS} heads")
    print(f"  - Feed Forward: d_model={D_MODEL} -> d_ff={D_FF} -> d_model={D_MODEL}")
    print(f"  - Output Projection: d_model={D_MODEL} -> vocab_size={len(tokenizer)}")
    
    model = GPTModel(
        vocab_size=len(tokenizer),
        d_model=D_MODEL,
        num_heads=NUM_HEADS,
        num_layers=NUM_LAYERS,
        d_ff=D_FF,
        dropout=DROPOUT,
        max_len=MAX_LEN,
        pad_idx=tokenizer.token_to_id["<pad>"]
    ).to(device)
    
    print(f"\nTotal Parameters: {count_params(model):,}")
    
    optimizer = optim.AdamW(model.parameters(), lr=LR, weight_decay=0.01)
    scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=EPOCHS)
    criterion = nn.CrossEntropyLoss(ignore_index=tokenizer.token_to_id["<pad>"])
    
    best_val_loss = float("inf")
    
    print("\n=== Training ===")
    print("Learning: predicting next token from context")
    print("Loss = CrossEntropy between predicted and actual next tokens\n")
    
    for epoch in range(EPOCHS):
        print(f"Epoch {epoch + 1}/{EPOCHS}")
        
        train_loss = train_epoch(model, train_loader, optimizer, criterion, device)
        val_loss = evaluate(model, val_loader, criterion, device)
        
        scheduler.step()
        
        print(f"Train Loss: {train_loss:.4f} | Val Loss: {val_loss:.4f}")
        
        if val_loss < best_val_loss:
            best_val_loss = val_loss
            torch.save({
                "epoch": epoch,
                "model_state_dict": model.state_dict(),
                "val_loss": val_loss,
                "config": {
                    "vocab_size": len(tokenizer),
                    "d_model": D_MODEL,
                    "num_heads": NUM_HEADS,
                    "num_layers": NUM_LAYERS,
                    "d_ff": D_FF,
                    "max_len": MAX_LEN
                }
            }, "gpt_best.pt")
            print("Saved best model!")
        print()
    
    print(f"=== Done! Best val loss: {best_val_loss:.4f} ===")

if __name__ == "__main__":
    main()
