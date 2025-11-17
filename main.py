import discord
from discord.ext import commands
import os

TOKEN = os.getenv("DISCORD_TOKEN")  # Używa ENV z Rendera
CHANNEL_ID = int(os.getenv("CHANNEL_ID", "0"))  # ID kanału np. 1397685283516055632

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

REACTIONS = ["❤️","1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟", "💯"]

@bot.event
async def on_ready():
    print(f"Bot zalogowany jako {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.channel.id == CHANNEL_ID:
        for emoji in REACTIONS:
            try:
                await message.add_reaction(emoji)
            except:
                pass

    await bot.process_commands(message)

bot.run(TOKEN)
