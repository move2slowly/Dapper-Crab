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
    
    if message.content.startswith('$register '):
        # Extract the username from the message content
        username = message.content.split('$register ')[1]
        # Register the user in the database   
        num_accounts = len(await check_registered_accounts(message.author))
        if(num_accounts >= config['max_user_accounts']):
            await message.channel.send(f'You have reached the max number of accounts allowed for your account.')
        else:
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

async def check_registered_accounts(discord_user):
    discord_name = str(discord_user) # This line is necessary because discord_user is a discord.member.Member type
    sqliteconn.execute("SELECT username FROM users WHERE discord_user = ?", (discord_name,))
    accounts = sqliteconn.fetchall()
    print(accounts)
    return accounts

client.run(config['discord_token'])