from flask import Flask, request, jsonify, send_from_directory
import torch
from tokenizer import BPETokenizer
from model import GPTModel

app = Flask(__name__, static_folder='.')

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
tokenizer = None
model = None

def load_model():
    global tokenizer, model
    
    print("Loading tokenizer...")
    tokenizer = BPETokenizer.load("tokenizer.pkl")
    
    print("Loading model...")
    checkpoint = torch.load("gpt_best.pt", map_location=device, weights_only=False)
    config = checkpoint["config"]
    
    model = GPTModel(
        vocab_size=config["vocab_size"],
        d_model=config["d_model"],
        num_heads=config["num_heads"],
        num_layers=config["num_layers"],
        d_ff=config["d_ff"],
        max_len=config["max_len"],
        pad_idx=tokenizer.token_to_id["<pad>"]
    ).to(device)
    
    model.load_state_dict(checkpoint["model_state_dict"])
    model.eval()
    
    print(f"Model loaded on {device}")

def generate_response(user_input, max_tokens=100, temperature=0.7):
    user_ids = [tokenizer.token_to_id["<user>"]] + tokenizer.encode(user_input)
    start_ids = user_ids + [tokenizer.token_to_id["<bot>"]]
    
    start_tensor = torch.tensor([start_ids], dtype=torch.long).to(device)
    
    with torch.no_grad():
        output = model.generate(
            start_tensor,
            max_new_tokens=max_tokens,
            temperature=temperature,
            top_k=40,
            top_p=0.9,
            eos_id=tokenizer.token_to_id["<eos>"]
        )
    
    output_ids = output[0].tolist()
    
    bot_idx = None
    for i, tok_id in enumerate(output_ids):
        if tok_id == tokenizer.token_to_id["<bot>"]:
            bot_idx = i
    
    if bot_idx is not None:
        response_ids = output_ids[bot_idx + 1:]
        response_ids = [t for t in response_ids if t not in [
            tokenizer.token_to_id["<eos>"],
            tokenizer.token_to_id["<pad>"]
        ]]
        return tokenizer.decode(response_ids)
    
    return tokenizer.decode(output_ids)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('.', path)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400
    
    response = generate_response(user_message)
    
    return jsonify({'response': response})

if __name__ == '__main__':
    load_model()
    print("\n" + "=" * 50)
    print("Server running at http://localhost:5000")
    print("=" * 50 + "\n")
    app.run(host='0.0.0.0', port=5000, debug=False)
