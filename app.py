from flask import Flask, render_template, request, jsonify, session
import requests
import secrets
import os

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Your Hugging Face API token
API_TOKEN = os.getenv('HF_TOKEN')
MODEL = "meta-llama/Llama-4-Scout-17B-16E-Instruct"
API_URL = f"https://router.huggingface.co/hf-inference/models/{MODEL}"

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
        
        # Format messages for the model
        messages_text = ""
        for msg in session['history']:
            role = msg['role'].capitalize()
            messages_text += f"{role}: {msg['content']}\n"
        messages_text += "Assistant:"
        
        # Call the API directly
        headers = {
            "Authorization": f"Bearer {API_TOKEN}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "inputs": messages_text,
            "parameters": {
                "max_new_tokens": 500,
                "temperature": 0.7,
                "return_full_text": False
            }
        }
        
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        
        result = response.json()
        
        # Extract the generated text
        if isinstance(result, list) and len(result) > 0:
            assistant_message = result[0].get('generated_text', '').strip()
        elif isinstance(result, dict):
            assistant_message = result.get('generated_text', '').strip()
        else:
            assistant_message = str(result)
        
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
        return jsonify({
            'error': str(e),
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
