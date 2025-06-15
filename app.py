import streamlit as st
from tests.text import obtener_respuesta

st.title("Hello, this is my new app!")

prompt = st.text_input("preguntale algo a gemini")

if st.button("Obtener respuesta"):
    respuesta= obtener_respuesta(prompt)
    st.text(respuesta)
    st.sucess("Mensaje generado")

