import streamlit as st
from langchain.agents import initialize_agent,AgentType
from langchain_groq import ChatGroq
from langchain_community.tools import WikipediaQueryRun,ArxivQueryRun,DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper,ArxivAPIWrapper
import os
from dotenv import load_dotenv
load_dotenv()
from langchain.callbacks import StreamlitCallbackHandler
st.title("🔎 LangChain - Chat with search")
"""
In this example, we're using `StreamlitCallbackHandler` to display the thoughts and actions of an agent in an interactive Streamlit app.
Try more LangChain 🤝 Streamlit Agent examples at [github.com/langchain-ai/streamlit-agent](https://github.com/langchain-ai/streamlit-agent).
"""

wiki=WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper(doc_content_chars_max=300))
arxiv=ArxivQueryRun(api_wrapper=ArxivAPIWrapper(doc_content_chars_max=300))

search=DuckDuckGoSearchRun(name="search",description="search when other tools don't give useful results")

tools=[wiki,arxiv,search]

st.sidebar.text("Enter your groq api key")
api_key=st.sidebar.text_input("Enter")

if "message" not in st.session_state:
    st.session_state['message']=[{"role":"assistant","content":"Hi,i am a chatbot.How can I help?"}]

for msg in st.session_state.message:
    st.chat_message(msg["role"]).write(msg["content"])

if chat_prompt:=st.chat_input(placeholder="Kya be?"):
    st.session_state.message.append({"role":"user","content":chat_prompt})
    st.chat_message("user").write(chat_prompt)
    llm=ChatGroq(api_key=api_key,model="gemma2-9b-it")
    agent=initialize_agent(tools=tools,llm=llm,agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION)

    with st.chat_message("assistant"):
        st_bc=StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
        response=agent.run(st.session_state.message,callbacks=[st_bc])
        st.session_state.message.append({'role':'assistant',"content":response})
        st.write(response)


