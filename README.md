# Dapper-Crab
## Setting up the bot
---
Set up the bot by first creating it in the discord developer portal using this link: https://discord.com/developers/applications
![alt text](image.png)
Then go to the bot tab and reset your token to get your bots token, then add your bot's token into the discord_token parameter in config.toml
![alt text](image-1.png)
Next check all of the privileged gateway intents on the same page:
![alt text](image-2.png)
Next in the OAuth2 tab add the bot scope and Administrator permission and copy the link generated below and paste it in a new window. Then invite the bot to your server!
![alt text](image-3.png)

# Running the Bot
---
```
pip install discord.py 
git clone https://github.com/move2slowly/Dapper-Crab
cd Dapper-Crab/dappercrab
python3 bot.py
```