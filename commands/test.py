from discord.ext import commands

class TestCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx):
        await ctx.send("This is test program")

def setup(bot):
    bot.add_cog(TestCommand(bot))
