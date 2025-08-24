import streamlit as st
from openai import OpenAI

# Initialize OpenAI
client = OpenAI(api_key="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")

st.title("🧮 Fariz's AI Math Tutor")

question = st.text_input("Enter your math problem:")

if st.button("Solve"):
    if question.strip() == "":
        st.warning("Please enter a math problem!")
    else:
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful math tutor."},
                    {"role": "user", "content": question},
                ]
            )
            answer = response.choices[0].message.content
            st.success(answer)
