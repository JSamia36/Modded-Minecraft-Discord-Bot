from nextcord import Interaction
from nextcord.ext import commands
from nextcord.ext.commands.core import has_permissions
import nextcord
from rcon.source import Client

# ---------CHANGE THESE-------------
TOKEN = 'PUT YOUR DISCORD BOT TOKEN HERE'
SERVER_ID = 'PUT YOUR SERVER ID HERE'
RCON_IP = '127.0.0.1'
RCON_PORT = '443'
RCON_PASSWD = 'SuperDuperSecret'
# ----------------------------------

special_chars = ['#', '|' , '&' , ';', ':', '(',')', '!']
intents = nextcord.Intents.default()
intents.message_content = True
intents.members = True

client = commands.Bot(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user} succesfully!')

@client.slash_command(name='whitelist', description='Whitelist a user in Minecraft', guild_ids=[SERVER_ID])
@commands.has_permissions(administrator=True)
async def whitelist(interaction: Interaction, mcusername: str):
    with Client(RCON_IP, RCON_PORT, passwd=RCON_PASSWD) as client:
        for i in special_chars:
            mcusername = mcusername.replace(i,"")
        response = client.run(f'whitelist add', mcusername)
        print(response)
        await interaction.response.send_message(f"Whitelisted {mcusername} successfully!")

@client.slash_command(name='kick', description='Kick a user in Minecraft', guild_ids=[SERVER_ID])
@commands.has_permissions(administrator=True)
async def whitelist(interaction: Interaction, mcusername: str):
    with Client(RCON_IP, RCON_PORT, passwd=RCON_PASSWD) as client:
        for i in special_chars:
            mcusername = mcusername.replace(i,"")
        response = client.run(f'kick', mcusername)
        print(response)
        await interaction.response.send_message(f"Kicked {mcusername} successfully!")


@client.slash_command(name='ban', description='Ban a user in Minecraft', guild_ids=[SERVER_ID])
@commands.has_permissions(administrator=True)
async def whitelist(interaction: Interaction, mcusername: str):
    with Client(RCON_IP, RCON_PORT, passwd=RCON_PASSWD) as client:
        for i in special_chars:
            mcusername = mcusername.replace(i,"")
        response = client.run(f'ban', mcusername)
        print(response)
        await interaction.response.send_message(f"Banned {mcusername} successfully!")

@client.slash_command(name='give', description='Give an item to a user in Minecraft', guild_ids=[SERVER_ID])
@commands.has_permissions(administrator=True)
async def whitelist(interaction: Interaction, mcusername: str, item: str, amount: str):
    with Client(RCON_IP, RCON_PORT, passwd=RCON_PASSWD) as client:
        for i in special_chars:
            mcusername = mcusername.replace(i,"")
        response = client.run(f'give', mcusername, item, amount)
        print(response)
        await interaction.response.send_message(f"Gave {mcusername} {amount} {item} successfully!")
