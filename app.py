from flask import Flask, render_template, request, jsonify, session
import requests
import secrets
import os
import time

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Your Hugging Face API token
API_TOKEN = os.getenv('HF_TOKEN')
MODEL = "meta-llama/Llama-4-Scout-17B-16E-Instruct:together"
API_URL = "https://router.huggingface.co/v1/chat/completions"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        
        # Get or create conversation history
        if 'history' not in session:
            session['history'] = []
        
        # Add user message to history
        session['history'].append({
            "role": "user",
            "content": user_message
        })
        
        # Call the API with automatic retries
        headers = {
            "Authorization": f"Bearer {API_TOKEN}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": MODEL,
            "messages": session['history'],
            "max_tokens": 500,
            "temperature": 0.7
        }
        
        # Retry up to 3 times for 503 errors
        max_retries = 3
        last_error = None
        
        for attempt in range(max_retries):
            try:
                response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
                
                if response.status_code == 503 and attempt < max_retries - 1:
                    print(f"Got 503, retrying... (attempt {attempt + 1}/{max_retries})")
                    time.sleep(2 ** attempt)  # Exponential backoff: 1s, 2s, 4s
                    continue
                
                response.raise_for_status()
                result = response.json()
                assistant_message = result['choices'][0]['message']['content']
                break
                
            except requests.exceptions.RequestException as e:
                last_error = e
                if attempt < max_retries - 1:
                    print(f"Request failed, retrying... (attempt {attempt + 1}/{max_retries})")
                    time.sleep(2 ** attempt)
                    continue
                else:
                    raise
        
        # Add assistant response to history
        session['history'].append({
            "role": "assistant",
            "content": assistant_message
        })
        
        # Keep only last 20 messages to manage context
        if len(session['history']) > 20:
            session['history'] = session['history'][-20:]
        
        session.modified = True
        
        return jsonify({
            'response': assistant_message,
            'status': 'success'
        })
        
    except Exception as e:
        import traceback
        error_details = traceback.format_exc()
        print(f"CHAT ERROR: {str(e)}")
        print(f"FULL TRACEBACK: {error_details}")
        
        # Return user-friendly error message
        error_msg = "The AI service is temporarily busy. Please try again in a moment."
        if "503" in str(e):
            error_msg = "The AI is experiencing high demand. Please wait a moment and try again."
        
        return jsonify({
            'error': error_msg,
            'status': 'error'
        }), 500

@app.route('/reset', methods=['POST'])
def reset():
    session['history'] = []
    session.modified = True
    return jsonify({'status': 'success', 'message': 'Conversation reset'})

if __name__ == '__main__':
    os.makedirs('templates', exist_ok=True)
    app.run(host='0.0.0.0', port=5001, debug=True)
