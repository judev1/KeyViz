from discord.ext import commands
from discord import File, Embed

desc = ("*Visualise encryption keys AND use them*\n\n**Commands**")

class help(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def _help(self, ctx):
        embed = Embed(title="KeyViz Help", description=desc, color=0xFF9999)
        embed.add_field(name="`!>key`",
                        value="Generates a key")
        embed.add_field(name="`!>vis ([key])`",
                        value="Visualises a key")
        embed.add_field(name="`!>encrypt (-key [key]) [text]`", inline=False,
                        value="Encrypts text using a random or specified key")
        embed.add_field(name="`!>decrypt [key] [text]`", inline=False,
                        value="Decrypts text using a specified key"
                              "\n\n**Here are some cool examples:**")
        embed.set_image(url="attachment://collage.png")
        collage = File("./imgs/collage.png")
        await ctx.send(embed=embed, file=collage)

def setup(bot):
    bot.add_cog(help(bot))
