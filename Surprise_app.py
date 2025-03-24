import streamlit as st

st.title("It's a surprise, just ask what it is lol")


user_question = st.text_input("Ask a question:")


answer = "I LOVE YOU KEMI!"

if user_question:
    st.write(f"Your Question: {user_question}")
    st.write(f"Answer: {answer}")