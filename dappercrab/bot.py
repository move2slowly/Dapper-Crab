import discord
import random

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$choose'):
        choicesarray = message.content[len('$choose '):]
        choicesarray = choicesarray.split(", ")
        option = random.choice(choicesarray)
        await message.channel.send ('I think' + ' ' + option + ' is the best option!')

    if message.content.startswith('$cat'):
        await message.channel.send('https://media.discordapp.net/attachments/845318731693555763/1082371108067623023/IMG_6446.gif')

client.run(discord_token)