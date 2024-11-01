# Unmaintained
This project was originally meant to teach a friend how to code. They are no longer interested in CS, this project will be deprecated until they are interested again.

# Dapper-Crab
## Setting up the bot
- Set up the bot by first creating it in the discord developer portal using this link: https://discord.com/developers/applications
- Then go to the bot tab and reset your token to get your bots token, then add your bot's token into the discord_token parameter in config.toml
- Next check all of the privileged gateway intents on the same page
- Next in the OAuth2 tab add the bot scope and Administrator permission and copy the link generated below and paste it in a new window. Then invite the bot to your server!
# Running the Bot
---
```
sudo apt update
pip install discord.py 
sudo apt install sqlite3
git clone https://github.com/move2slowly/Dapper-Crab
cd Dapper-Crab/dappercrab
sqlite3 users //in the next following commands use them in the sqlite3 cli
	.read init.sql
	.exit
python3 bot.py
```
