import os
import openai
import streamlit as st


def api_connection(api_key_val="OPENAI_API_KEY"):

    # Set API key for OpenAI
    openai.api_key = st.secrets[api_key_val]


def lang_model_output(prompt_text=None):

    print("Building connection..")
    api_connection()

    print("Runnig model..")
    model_response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt_text,
        temperature=0.7,
        max_tokens=1204,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=1
    )

    return model_response.choices[0].text
        
