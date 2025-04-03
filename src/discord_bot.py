import discord
from discord.ext import commands
from config.settings import DISCORD_TOKEN

# Botの設定
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)

# Bot起動時に呼ばれるイベント
@bot.event
async def on_ready():
    print(f"✅ {bot.user.name} がログインしました！")

# Botでメッセージを送信する関数
async def send_discord_notification(channel_id, message):
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send(message)
    else:
        print(f"❌ チャンネルID {channel_id} が見つかりませんでした。")

# Botの実行
def start_discord_bot():
    bot.run(DISCORD_TOKEN)
