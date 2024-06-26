from dotenv import load_dotenv
import os

from langchain_groq import ChatGroq
from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')
groq_api_key = os.getenv('GROQ_API_KEY')


prompt = "Tengo que hacer un trabajo final de un curso de LLM, dame 3 ideas para ser utilizadas \
como trabajo final"


def get_response(tipo, prompt, temperature=0):
    if tipo == "openai":
        llm = ChatOpenAI(temperature=temperature, model_name="gpt-3.5-turbo", api_key=openai_api_key)
    elif tipo == "groq":
        llm = ChatGroq(temperature=temperature, model="llama3-70b-8192", api_key=groq_api_key)
    elif tipo == "anthropic":
        llm = ChatAnthropic(temperature=temperature, model='claude-3-opus-20240229', api_key=anthropic_api_key)
    
    respuesta = llm.invoke(prompt)

    return print(respuesta.content)


print("Respuesta GPT3.5 Turbo\n----------------")
get_response("openai", prompt)

print("\nRespuesta Llama 3\n----------------")
get_response("groq", prompt)

# print("\nRespuesta Claude 3\n----------------")
# get_response("anthropic", prompt)