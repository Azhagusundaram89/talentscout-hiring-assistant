import requests

import os
API_KEY = os.getenv("GROQ_API_KEY")


def get_llm_response(prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code != 200:
        return f"Error: {response.text}"

    return response.json()["choices"][0]["message"]["content"]