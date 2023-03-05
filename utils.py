import os
import openai


def api_connection(api_key_val="OPENAI_API_KEY"):

    api_key = os.getenv(api_key_val)
    openai.api_key = api_key

def lang_model_output(prompt_text=None):

    print("Getting API Key..")
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
        
