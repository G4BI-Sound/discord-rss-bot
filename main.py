import discord
import asyncio

TOKEN = "IL_TUO_TOKEN_DISCORD"

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

rss_feeds = [
    "https://rss-bridge-animespotlight.onrender.com/?action=display&bridge=InstagramBridge&context=Username&u=animespotlight&media_type=all&format=Atom",
    "https://rss-bridge-animespotlight.onrender.com/?action=display&bridge=InstagramBridge&context=Username&u=jpopmanga&media_type=all&format=Atom",
    "https://rss-bridge-animespotlight.onrender.com/?action=display&bridge=InstagramBridge&context=Username&u=panini_planetmanga&media_type=all&format=Atom",
    "https://rss-bridge-animespotlight.onrender.com/?action=display&bridge=InstagramBridge&context=Username&u=edizionistarcomics&media_type=all&format=Atom"
]

channel_id = 1389047949509787698

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

client.run(TOKEN)