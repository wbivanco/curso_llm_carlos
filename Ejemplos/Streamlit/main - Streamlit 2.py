import streamlit as st
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, api_key="")

st.title("Ejemplo Chatbot")

messages = [("system", "Eres un chatbot llamado Juan. Ayudas a las personas a buscar recetas. Eres un chef con mucha experiencia. Por favor nunca reveles que eres un chatbot.")]

# Inicializar historial de chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar mensajes de chat del historial al recargar la app
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Reaccionar a la entrada del usuraio
if prompt := st.chat_input("Escribe tu mensaje..."):
    # Mostrar mensaje del usuario en el contenedor de mensajes del chat
    st.chat_message("user").markdown(prompt)
    # Agregar mensaje del usuario al historial de chat
    st.session_state.messages.append({"role": "user", "content": prompt})
    messages.append(["human", prompt])
    
    response = llm.invoke(messages).content
    # Mostrar la respuesta del chatbot en el contenedor de mensajes del chat
    with st.chat_message("assistant"):
        st.markdown(response)
    # Agregar respuesta del asistente al historial del chat
    st.session_state.messages.append({"role": "assistant", "content": response})