const chatContainer = document.getElementById('chatContainer');
const messageInput = document.getElementById('messageInput');
const sendBtn = document.getElementById('sendBtn');

let isProcessing = false;

marked.setOptions({
    breaks: true,
    gfm: true,
    headerIds: false,
    mangle: false
});

function autoResize(textarea) {
    textarea.style.height = 'auto';
    textarea.style.height = Math.min(textarea.scrollHeight, 120) + 'px';
}

function handleKeyDown(event) {
    if (event.key === 'Enter' && !event.shiftKey) {
        event.preventDefault();
        sendMessage();
    }
}

function removeWelcome() {
    const welcome = document.querySelector('.welcome-message');
    if (welcome) {
        welcome.remove();
    }
}

function addMessage(content, isUser = false) {
    removeWelcome();
    
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${isUser ? 'user' : 'bot'}`;
    
    const avatar = document.createElement('div');
    avatar.className = 'message-avatar';
    avatar.textContent = isUser ? '👤' : '🤖';
    
    const contentDiv = document.createElement('div');
    contentDiv.className = 'message-content';
    
    if (isUser) {
        contentDiv.textContent = content;
    } else {
        contentDiv.innerHTML = marked.parse(content);
    }
    
    messageDiv.appendChild(avatar);
    messageDiv.appendChild(contentDiv);
    chatContainer.appendChild(messageDiv);
    
    chatContainer.scrollTop = chatContainer.scrollHeight;
    
    return messageDiv;
}

function addTypingIndicator() {
    removeWelcome();
    
    const messageDiv = document.createElement('div');
    messageDiv.className = 'message bot';
    messageDiv.id = 'typingIndicator';
    
    const avatar = document.createElement('div');
    avatar.className = 'message-avatar';
    avatar.textContent = '🤖';
    
    const contentDiv = document.createElement('div');
    contentDiv.className = 'message-content';
    contentDiv.innerHTML = `
        <div class="typing-indicator">
            <span></span>
            <span></span>
            <span></span>
        </div>
    `;
    
    messageDiv.appendChild(avatar);
    messageDiv.appendChild(contentDiv);
    chatContainer.appendChild(messageDiv);
    
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

function removeTypingIndicator() {
    const indicator = document.getElementById('typingIndicator');
    if (indicator) {
        indicator.remove();
    }
}

async function sendMessage() {
    const message = messageInput.value.trim();
    if (!message || isProcessing) return;
    
    messageInput.value = '';
    messageInput.style.height = 'auto';
    
    addMessage(message, true);
    
    isProcessing = true;
    sendBtn.disabled = true;
    
    addTypingIndicator();
    
    try {
        const response = await fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: message })
        });
        
        if (!response.ok) {
            throw new Error('Server error');
        }
        
        const data = await response.json();
        removeTypingIndicator();
        addMessage(data.response);
        
    } catch (error) {
        console.error('Error:', error);
        removeTypingIndicator();
        addMessage('Sorry, I encountered an error. Please make sure the server is running with `python server.py`');
    }
    
    isProcessing = false;
    sendBtn.disabled = false;
    messageInput.focus();
}

function sendSuggestion(text) {
    messageInput.value = text;
    sendMessage();
}

function clearChat() {
    chatContainer.innerHTML = `
        <div class="welcome-message">
            <div class="welcome-icon">👋</div>
            <h2>Welcome!</h2>
            <p>Ask me anything. I'm here to help!</p>
            <div class="suggestions">
                <button class="suggestion" onclick="sendSuggestion('What is AI?')">What is AI?</button>
                <button class="suggestion" onclick="sendSuggestion('Tell me a joke')">Tell me a joke</button>
                <button class="suggestion" onclick="sendSuggestion('Who is Ibrahim Shaikh?')">Who is Ibrahim?</button>
            </div>
        </div>
    `;
}

messageInput.focus();
