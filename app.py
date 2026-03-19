import streamlit as st

st.title("🤖 My AI Chatbot (Free Version)")

# chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# display messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# input
user_input = st.chat_input("Ask something...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    # simple rule-based replies
    if "hello" in user_input.lower():
        answer = "Hi! How can I help you? 😊"
    elif "python" in user_input.lower():
        answer = "Python is a popular programming language used for AI and development."
    elif "ai" in user_input.lower():
        answer = "AI means Artificial Intelligence — machines that can think and learn."
    else:
        answer = "I'm still learning 😅 please ask something simple."

    st.session_state.messages.append({"role": "assistant", "content": answer})
    st.chat_message("assistant").write(answer)
