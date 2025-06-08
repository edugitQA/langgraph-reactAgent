from langgraph.prebuilt import create_react_agent
from langchain_core.messages import SystemMessage
from langchain_core.tools import Tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools.tavily_search import TavilySearchResults
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.8,
    api_key=API_KEY,
)

system_message = SystemMessage(content="""Você é o bot pesquisa.
                                Você tem acesso a ferramentas para buscar informações na web.
                                Você deve usar essas ferramentas para buscar informações sobre o assunto que o usuário perguntar.
                                Você deve responder de forma clara e objetiva.""")

@tool
def search_web(query: str) -> str:
    """Busca informações na web baseada na consulta fornecida.
    Args:
        query (str): Termos para busca na web.
    
    Returns:
        As informações encontradas na web ou uma mensagem indicando que nada foi encontrado.
    """
    tavily_search = TavilySearchResults(max_results=3)
    search_docs =  tavily_search.invoke(query)
    return search_docs

#lista de ferramentas talvez até MCP
tools = [search_web]


# Agente React com memoria
graph = create_react_agent(
    model,
    tools=tools,
    prompt=system_message,
)