import streamlit as st
import requests

# Backend API URL
API_URL = "http://backend:8000/chat"

st.set_page_config(page_title="Mental Health AI", layout="centered")

st.title("🧠 Mental Health AI Assistant")
st.caption("Talk freely. I'm here to listen.")

# 🔥 STEP 1: Ask user name FIRST
if "user_id" not in st.session_state:
    name = st.text_input("Enter your name to start:")

    if name:
        st.session_state.user_id = name
        st.session_state.messages = []
        st.rerun()
    else:
        st.stop()

# 🔥 Sidebar (optional but useful)
with st.sidebar:
    st.header("👤 User Info")
    st.write(f"Logged in as: {st.session_state.user_id}")

    if st.button("🔄 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# 🔥 Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# 🔥 Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 🔥 Chat input
user_input = st.chat_input("How are you feeling today?")

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    # 🔥 Call backend
    try:
        response = requests.post(
            API_URL,
            json={
                "user_id": st.session_state.user_id,
                "message": user_input
            },
            timeout=30
        )

        data = response.json()
        reply = data.get("reply", "No response from AI")
        emotion = data.get("emotion", "unknown")

    except Exception as e:
        print("ERROR:", e)
        reply = "⚠️ Backend not responding."
        emotion = "unknown"

    # 🔥 Format AI response
    ai_message = reply

    # Save AI response
    st.session_state.messages.append({
        "role": "assistant",
        "content": ai_message
    })

    # Display AI response
    with st.chat_message("assistant"):
        st.markdown(ai_message)