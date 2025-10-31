from flask import Flask, render_template, request, jsonify, session
from huggingface_hub import InferenceClient
import secrets
import os

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Your Hugging Face API token
API_TOKEN = os.getenv('HF_TOKEN')
client = InferenceClient(token=API_TOKEN)
MODEL = "meta-llama/Llama-4-Scout-17B-16E-Instruct"

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
        
        # Get response from Llama 4 Scout using text_generation
        response_text = client.text_generation(
            messages_text,
            model=MODEL,
            max_new_tokens=500,
            temperature=0.7
        )
        
        assistant_message = response_text.strip()
        
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
