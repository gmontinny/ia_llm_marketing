from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from src.config import (
    GROQ_API_KEY, MODEL_NAME,
    OPENAI_API_KEY, OPENAI_MODEL,
    TEMPERATURE,
)
from src.prompts import SYSTEM_PROMPT, ContentRequest, build_user_prompt


def get_llm(provider: str = "Groq (Llama)"):
    """Factory que retorna a LLM com base no provedor selecionado."""
    if provider == "OpenAI (ChatGPT)":
        return ChatOpenAI(
            model=OPENAI_MODEL,
            temperature=TEMPERATURE,
            api_key=OPENAI_API_KEY,
            max_retries=2,
        )
    return ChatGroq(
        model=MODEL_NAME,
        temperature=TEMPERATURE,
        api_key=GROQ_API_KEY,
        max_retries=2,
    )


def generate_content(request: ContentRequest, provider: str = "Groq (Llama)") -> str:
    """Gera conteudo usando a chain: template -> llm -> parser."""
    llm = get_llm(provider)

    template = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ("human", "{prompt}"),
    ])

    chain = template | llm | StrOutputParser()

    user_prompt = build_user_prompt(request)
    return chain.invoke({"prompt": user_prompt})
