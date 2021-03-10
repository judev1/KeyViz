from discord.ext import commands
from discord import File, Embed
import imggen
import os

desc = ("*Visualise encryption keys AND use them*\n\n**Commands**")

class vis(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="vis")
    async def _vis(self, ctx, *args):

        await ctx.channel.trigger_typing()

        text = None
        user_id = ctx.author.id
        if args:
            text = " ".join(args)
            if len(text) > 1500:
                await ctx.send("Keys cannot exceed 1500 characters")
                return
            text = bytes(text, encoding="utf_8")

        text = imggen.gen(f"./imgs/temp/{user_id}", text)
        img = File(f"./imgs/temp/{user_id}.png")

        embed = Embed(title="KeyViz Visualiser", color=0xFF9999)
        embed.add_field(name="Key:", value=f"```yaml\n{text}```")
        embed.set_image(url=f"attachment://{user_id}.png")

        await ctx.send(embed=embed, file=img)

        os.remove(f"./imgs/temp/{user_id}.png")
        

def setup(bot):
    bot.add_cog(vis(bot))
