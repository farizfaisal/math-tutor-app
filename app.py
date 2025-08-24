import streamlit as st
from openai import OpenAI

# App title
st.title("🧮 Fariz's AI Math Tutor")

# Store API key securely in session state
if "api_key" not in st.session_state:
    st.session_state.api_key = ""

st.session_state.api_key = st.text_input(
    "Enter your OpenAI API Key:",
    type="password"
)

# Only initialize client if key is provided
if st.session_state.api_key:
    client = OpenAI(api_key=st.session_state.api_key)

    # Math input
    problem = st.text_input("Enter your math problem:")

    if st.button("Solve") and problem:
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful math tutor. Explain step by step."},
                    {"role": "user", "content": problem}
                ]
            )
        st.success(response.choices[0].message.content)

else:
    st.info("🔑 Please enter your OpenAI API key to continue.")
