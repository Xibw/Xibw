import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# 環境変数読み込み
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Botの設定
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)

# 起動時に表示
@bot.event
async def on_ready():
    print(f"[起動成功] Bot名: {bot.user.name} | ID: {bot.user.id}")

# コマンド読み込み
bot.load_extension("commands.ping")

# Bot開始
bot.run(TOKEN)
