import os
import discord
from discord import Client, Intents, Bot
# nie importuj modułów związanych z voice

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
bot = commands.Bot(command_prefix="!", intents=intents)

# ID kanału #ocenka-bitow
TARGET_CHANNEL = 1397685283516055632

# Lista reakcji
reactions = ['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣','🔟','💯']

@bot.event
async def on_ready():
    print(f"Bot zalogowany jako: {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if message.channel.id != TARGET_CHANNEL:
        return
    for emoji in reactions:
        try:
            await message.add_reaction(emoji)
        except Exception as e:
            print(f"Błąd dodawania reakcji: {e}")

    await bot.process_commands(message)

bot.run(TOKEN)
