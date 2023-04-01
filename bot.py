import discord
import responses


async def send_message(message):
    try:
        response = responses.get_response()
        await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = 'insert token here'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if str(message.author) == 'callmedaddy420#4175':
            await send_message(message)

    client.run(TOKEN)
