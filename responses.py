from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

ai_model = OllamaLLM(model = "llama3.1")
ai_template = """
user: {ai_user}
Chat history: {ai_chat_history}
Answer the user input.
User input: {ai_input}
"""
ai_prompt = ChatPromptTemplate.from_template(ai_template)
ai_chain = ai_prompt | ai_model
ai_chat_history = ""

def get_response(message: str) -> str:
    response = ai_chain.invoke({"ai_chat_history": ai_chat_history, "ai_input": message})
    ai_chat_history += f"\nuser: {message}\n \nYou: {response}"
    return response