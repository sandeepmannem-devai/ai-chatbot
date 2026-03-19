import streamlit as st

st.title("✨ AI Content Generator")

topic = st.text_input("Enter topic:")

if topic:
    st.write("### Generated Content")

    caption = f"🔥 {topic.capitalize()} is the key to success! Stay consistent 💪"
    title = f"Top 5 Tips for {topic.capitalize()}"
    idea = f"Create a daily routine about {topic} and share your progress"

    st.write("📸 Caption:", caption)
    st.write("🎬 Title:", title)
    st.write("💡 Idea:", idea)