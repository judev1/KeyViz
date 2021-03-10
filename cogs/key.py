from cryptography.fernet import Fernet
from discord.ext import commands
from discord import Embed

desc = ("*Visualise encryption keys AND use them*\n\n**Commands**")

class key(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="key")
    async def _key(self, ctx):

        key = str(Fernet.generate_key())[2:-1]
        key = f"```yaml\n{key}```"
        embed = Embed(title="KeyViz Key", description=key, color=0xFF9999)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(key(bot))
