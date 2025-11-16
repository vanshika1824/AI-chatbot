import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load .env locally (Streamlit Cloud will use Secrets instead)
load_dotenv()

st.title("🤖 AI Chatbot (LLM Project)")
st.write("A simple Streamlit web interface for OpenAI LLM")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

user_input = st.text_input("You:", "")

if st.button("Send"):
    if user_input.strip() == "":
        st.warning("Please type something!")
    else:
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": user_input}]
            )
            reply = response.choices[0].message.content
            st.success(reply)
