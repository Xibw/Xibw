import discord
from discord.ext import commands
import json
import os

DATA_FILE = "data.json"

# データを読み込む関数
def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

# データを保存する関数
def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

class LinkCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def link(self, ctx, platform: str, url: str):
        """ユーザーのX, Youtube, Instagram, Twitchのリンクを登録"""
        platform = platform.lower().capitalize()  # 最初の文字を大文字に統一
        if platform not in ["X", "Youtube", "Instagram", "Twitch"]:
            await ctx.send("対応しているプラットフォームは X, Youtube, Instagram, Twitch です。")
            return

        user_id = str(ctx.author.id)
        data = load_data()

        if user_id not in data:
            data[user_id] = {}

        data[user_id][platform] = url
        save_data(data)

        await ctx.send(f"{platform} のリンクを登録しました: {url}")

def setup(bot):
    bot.add_cog(LinkCommands(bot))
