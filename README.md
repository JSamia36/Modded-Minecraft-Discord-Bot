# Modded-Minecraft-Discord-Bot
Run commands easily from a discord channel! They will all be ran directly on your minecraft server

# Requirements
- Python
- Discord Bot Token
- Ability to host discord bot

# Setup
1) Get a discord token from [here](https://discord.com/developers/applications)
2) Install all required libraries, we are just using two for this
3) I highly recommend hosting the bot locally as I will take about later with the potential security concerns
4) Make sure RCON is enabled in your minecraft folder. It should be under server.properties, you will need to set a port and password as well.

# Getting Started
```
pip install -r requirements.txt
```
Modify main.py, you need to add your IP, port, password for RCON. Then I highly recommend setting guild_ids as otherwise commands can be ran by other servers. Currently it is setup so only admins can isue the commands but you can modify if you need. This is just a barebone discord bot to issue commands on your server. Once that is modified just run:
```
python3 main.py
```

# Security Concerns
Please note that RCON is not the most secure. Because of this I don't recommend opening the port up. Instead just run the discord bot locally or on the same server as Minecraft. Currently I only have a very basic filter for removing symbols, again this is just a barebone framework you can build upon. Most people won't need more than this and if they do are likely more experienced in developing than me. 
