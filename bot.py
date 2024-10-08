import discord
import responses
import dotenv
import os

async def send_message(message, user_message, is_private, user):
    try:
        response = responses.get_response(user_message, user=user)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)

def run_discord_bot():
    dotenv.load_dotenv()
    TOKEN = os.getenv('DISCORD_BOT_TOKEN')
    print("Discord bot token: " + TOKEN)
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True, user=username)
        else:
            if channel != 'general':
                await send_message(message, user_message, is_private=False, user=username)

    client.run(TOKEN)