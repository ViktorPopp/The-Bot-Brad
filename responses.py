import openai
import dotenv

dotenv.load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

def get_response(message: str) -> str:
    p_message = message.lower()

    try:
        response = openai.Completion.create(
            model = 'gpt3.5-turbo',
            messages = [{'role': 'user', 'content': message}]
        )
        return response.choices[0].text.strip()

    except:
        return 'Sorry, something went wrong Error code: 1. Contact the owner of this server for help.'