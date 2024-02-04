# from dotenv import load_dotenv
# load_dotenv()

import streamlit as st
from langchain_openai import ChatOpenAI


chat_model =ChatOpenAI()

st.title('AI Prof')

content=st.text_input("Type your question below")

if st.button('Find Answer'):
    with st.spinner('Finding you a solution...'):
        result=chat_model.invoke("Please provide an answer with detailed information regarding this question : " + content)
        st.write(result)



