import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/X ', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def test(ctx):
    await ctx.send("This is test program")

bot.run('YOUR_DISCORD_TOKEN')  # 実際のBotトークンに置き換える
