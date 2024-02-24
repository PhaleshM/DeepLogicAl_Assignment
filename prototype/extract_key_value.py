import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()



def generate(text,doc_type):

    API_key=os.getenv("GEMINI_API_KEY")

    genai.configure(api_key=API_key)

    # Set up the model
    generation_config = {
        "temperature": 0,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
    }

    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        }
    ]

    model = genai.GenerativeModel(model_name="gemini-pro",
                                  generation_config=generation_config,
                                  safety_settings=safety_settings)


    if doc_type=='t':
    #     prompt = f'''Analyse the text and extract data of table.
    # response should be in this format: "header_data=[column1,column2,column3,.....]
    # table_data=[(row1,.....),(row2,....),(row3,.....)]"
    # text:- {text}'''
        # prompt = f'''Analyse the text and extract data from table.
        # response should be in csv format."
        # text:- {text}'''
        prompt = '''Analyse the text and extract data from table.
        response should be in python dictionary like dictionary_name={'key1':'value1','key2':'value2'}
        text:- "'''+text+'"'
        
    else:
        prompt = f'''Analyse the text and return the text in detail. Response should be in paragraphs markdown format.
    text:- {text}'''
        # prompt = f'''Analyse the text and the rewrite it without any neamingfull words. 
        # text:- ""{text}""'''

    response = model.generate_content(prompt)
    result_parts = response.parts
    text=""
    for part in result_parts:
        # print("part\n",part.text)
        text+=str(part.text)
    return text

