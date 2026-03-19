import streamlit as st

st.title("🤖 My AI Chatbot (Free Version)")

# create memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# show previous messages
for msg in st.session_state.messages:
    st.write(msg)

# user input
user_input = st.text_input("Ask something:")

if user_input:
    # store user message
    st.session_state.messages.append("You: " + user_input)

    # simple replies
    if "hello" in user_input.lower():
        reply = "Hi! How can I help you? 😊"
    elif "python" in user_input.lower():
        reply = "Python is a programming language used for AI and development."
    elif "ai" in user_input.lower():
        reply = "AI means Artificial Intelligence 🤖"
    else:
        reply = "I'm still learning 😅 please ask something simple."

    # store bot reply
    st.session_state.messages.append("Bot: " + reply)

    # show reply
    st.write("Bot:", reply)
