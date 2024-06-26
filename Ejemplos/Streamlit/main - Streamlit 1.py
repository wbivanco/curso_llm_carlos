import streamlit as st
from langchain import PromptTemplate
from langchain_openai import OpenAI


template = """
    Por favor traduce el siguiente texto: {texto}, del idioma {idioma_entrada} al idioma {idioma_salida}
"""

#Definición de variables para el PromptTemplate
prompt = PromptTemplate(
    input_variables=["texto", "idioma_entrada", "idioma_salida"],
    template=template,
)


#Función de carga de LLM y API Key
def load_LLM(openai_api_key):
    llm = OpenAI(temperature=0, openai_api_key=openai_api_key)
    return llm


#Título y encabezado de la página
st.set_page_config(page_title="Traduce tu text")
st.header("Traduce tu texto")


#Input OpenAI API Key
st.markdown("## Ingresa tu API Key de OpenAI")

def get_openai_api_key():
    input_text = st.text_input(label="API Key de OpenAI",  placeholder="Ejemplo: sk-2twmA8tfCb8un4...", key="openai_api_key_input", type="password")
    return input_text

openai_api_key = get_openai_api_key()


# Input
st.markdown("## Ingresa el texto que deseas traducir")

def get_texto():
    draft_text = st.text_area(label="Texto", label_visibility='collapsed', placeholder="Tu texto...", key="draft_input")
    return draft_text

texto = get_texto()

if len(texto.split(" ")) > 700:
    st.write("Por favor ingresa un texto más corto. La extensión máxima es de 700 palabras.")
    st.stop()

# Prompt template tunning options
col1, col2 = st.columns(2)
with col1:
    idioma_entrada = st.selectbox(
        'Idioma de entrada',
        ('Inglés', 'Español', 'Italiano', 'Francés', 'Portugués', 'Alemán'))
    
with col2:
    idioma_salida = st.selectbox(
        'Idioma de salida',
        ('Inglés', 'Español', 'Italiano', 'Francés', 'Portugués', 'Alemán'))
    
    
# Output
st.markdown("### Tu texto traducido:")

if texto:
    if not openai_api_key:
        st.warning('Por favor ingresa tu API Key de OpenAI.', 
            icon="⚠️")
        st.stop()

    llm = load_LLM(openai_api_key=openai_api_key)

    traduccion_prompt = prompt.format(
        texto=texto,
        idioma_entrada=idioma_entrada, 
        idioma_salida=idioma_salida
    )

    traduccion = llm(traduccion_prompt)

    st.write(traduccion)