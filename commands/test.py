import discord
from discord.ext import commands

# /ibw test コマンドの処理
@commands.command()
async def test(ctx):
    await ctx.send("This is test program")

# Botにコマンドを登録する関数
def setup(bot):
    bot.add_command(test)

