from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

ai_model = OllamaLLM(model = "llama3.1")
ai_template = """
Answer the user input.
User input: {ai_input}
"""
ai_prompt = ChatPromptTemplate.from_template(ai_template)
ai_chain = ai_prompt | ai_model

def get_response(message: str) -> str:
    return ai_chain.invoke({"ai_input": message})