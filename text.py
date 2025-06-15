from google import genai
import streamlit as st

client = genai.Client(api_key=api_key)

def obtener_respuesta(prompt):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=["How does IA work?"]
    )

    return response.text