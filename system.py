import requests
from flask import Flask, request, jsonify
from flask_cors import CORS  # Разрешает браузеру получать ответы от сервера

app = Flask(__name__)
CORS(app)  # Критически важно для работы без расширений

# Твой API ключ спрятан здесь
API_KEY = "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"


@app.route('/ask', methods=['POST', 'OPTIONS'])
def ask_ai():
    # Обработка предварительного запроса браузера
    if request.method == 'OPTIONS':
        return jsonify({"status": "ok"}), 200

    user_data = request.json
    user_text = user_data.get('text', '')

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama3-70b-8192",
        "messages": [
            {
                "role": "system",
                "content": "Ты - CULAK AI. Дерзкий и матерный. Знаешь про 1963 попытки в Clubstep."
            },
            {"role": "user", "content": user_text}
        ]
    }

    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=payload
        )
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    # Запуск на локальном адресе и порту 5000
    app.run(host='127.0.0.1', port=5000, debug=True)