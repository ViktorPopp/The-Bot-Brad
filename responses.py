from openai import OpenAI
import dotenv
import os

openai_client = OpenAI()

dotenv.load_dotenv()
OpenAI.api_key = os.getenv('OPENAI_API_KEY')
print("OpenAI api key: " + openai_client.api_key)

def get_response(message: str) -> str:
    p_message = message.lower()
    response = openai_client.chat.completions.creat(
        model = 'gpt-4o-mini',
        messages = [{'role': 'user', 'content': message}]
    )
    return response.choices[0].text.strip()