import streamlit as st
import requests
import re

OLLAMA_MODEL = "qwen2.5-coder:0.5b"

def rule_based_filter(text):
    t = text.lower().strip()

    harmless_patterns = [
        r"what is religion",
        r"define religion",
        r"types of religion",
        r"history of religion",
        r"what is a bomb calorimeter",        # scientific
        r"sex ratio",                          # demographic
        r"sexual reproduction in plants",      # biology
    ]
    for pattern in harmless_patterns:
        if re.search(pattern, t):
            return None  
    

    sensitive_rules = {
        "hacking": "I cannot provide hacking-related help.",
        "hack": "I cannot assist with hacking.",
        
        "bomb": "Weapons or explosive-related information is restricted.",
        "explosive": "Explosive-related information is restricted.",
        "make bomb": "Weapons or explosive-related information is restricted.",
        "build bomb": "Weapons or explosive-related information is restricted.",


        "how to kill": "Violence-related information is restricted.",

        "sexual": "Sexual content is restricted.",
        "nude": "Explicit content cannot be provided.",
        
        "terrorist": "Extremism-related topics cannot be discussed.",
        "terrorism": "Extremism-related topics cannot be discussed.",

        "hate speech": "Hate speech is strictly prohibited.",
    }

    harmful_patterns = [
        r"how to make.*bomb",
        r"how to build.*weapon",
        r"how to hack",
        r"how can i hack",
        r"kill someone",
        r"how to kill",
        r"sexual content",
        r"send nudes",
        r"terrorist attack",
    ]


    for pattern in harmful_patterns:
        if re.search(pattern, t):
            return "This request is not allowed due to harmful content."

    # Then check sensitive keywords (fallback)
    for key, msg in sensitive_rules.items():
        if key in t:
            return msg

    return None


def call_ollama(prompt_text):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": OLLAMA_MODEL,
            "prompt": prompt_text,
            "stream": False
        }
    )
    data = response.json()
    return data.get("response", "Error: No response from model")



# STREAMLIT UI APP
st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

st.title("🤖 Local AI Chatbot using Ollama")
st.caption("Running model: **" + OLLAMA_MODEL + "**")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])


# User Input
user_input = st.chat_input("Ask anything...")


if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    rule_result = rule_based_filter(user_input)

    if rule_result:
        reply = rule_result
    else:
         with st.spinner("Thinking..."):
                reply = call_ollama(user_input)

    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)
