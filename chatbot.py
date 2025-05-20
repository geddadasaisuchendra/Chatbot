import streamlit as st
import requests
import json

# Your OpenRouter API key
API_KEY = "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"

st.title("🤖 Chat with AI")
st.write("Using the `deepseek/deepseek-r1:free model`")

# Input from user
user_input = st.text_input("Ask something:")

if st.button("Send") and user_input:
    # Prepare the request
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "deepseek/deepseek-r1:free",
        "messages": [
            {"role": "user", "content": user_input}
        ]
    }

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            data=json.dumps(payload)
        )
        result = response.json()
        message = result["choices"][0]["message"]["content"]
        st.success("Response:")
        st.write(message)
    except Exception as e:
        st.error(f"Something went wrong: {e}")
