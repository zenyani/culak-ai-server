import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

# Твой новый ключ, который ты скинул
API_KEY = "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"

@app.route('/ask', methods=['POST', 'OPTIONS'])
def ask_ai():
    if request.method == 'OPTIONS':
        return jsonify({"status": "ok"}), 200

    user_data = request.json
    user_text = user_data.get('text', '')

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "system", "content": "Ты — CULAK AI, дерзкий и крутой помощник. Отвечай по делу."},
            {"role": "user", "content": user_text}
        ]
    }

    try:
        response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)
        data = response.json()
        print("Ответ от Groq:", data) 
        return jsonify(data)
    except Exception as e:
        print(f"Ошибка: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
