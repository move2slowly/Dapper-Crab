import discord
import sqlite3
import random
import toml

intents = discord.Intents.default()
intents.message_content = True

# Initialize Discord Client
client = discord.Client(intents=intents)

# Connect to sqlite3 database
conn = sqlite3.connect('users')
sqliteconn = conn.cursor()

# Load toml file
with open('config.toml', 'r') as f:
    config = toml.load(f)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
    if message.content.startswith('/register '):
        # Extract the username from the message content
        username = message.content.split('/register ')[1]
        
        # Register the user in the database
        await register_user(message.author, username)
        await message.channel.send(f'User {username} has been registered.')

    if message.content.startswith('$choose'):
        choicesarray = message.content[len('$choose '):]
        choicesarray = choicesarray.split(", ")
        option = random.choice(choicesarray)
        await message.channel.send ('I think' + ' ' + option + ' is the best option!')

    if message.content.startswith('$cat'):
        await message.channel.send('https://media.discordapp.net/attachments/845318731693555763/1082371108067623023/IMG_6446.gif')

async def register_user(discord_user, username):
    discord_name = str(discord_user) # This line is necessary because discord_user is a discord.member.Member type
    sqliteconn.execute("INSERT INTO users (discord_user, username) VALUES (?, ?)", (discord_name, username))
    conn.commit()

client.run(discord_token)