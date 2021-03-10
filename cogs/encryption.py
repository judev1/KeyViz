from cryptography.fernet import Fernet
from discord.ext import commands
from discord import Embed

class encryption(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="encrypt")
    async def _encrypt(self, ctx, *args):

        await ctx.channel.trigger_typing()

        if args:
            args = list(args)
            key = Fernet.generate_key()
            if args[0].lower() == "-key":
                args.pop(0)
                if args:
                    key = bytes(args[0], encoding="utf_8")
                    args.pop(0)
                else:
                    await ctx.send("You never specified the key!")
            if args:
                text = " ".join(args)
                if len(text) <= 500:
                    try:
                        lock = Fernet(key)
                        text = bytes(text, encoding="utf_8")
                        etext = str(lock.encrypt(text))[2:-1]

                        key = f"```yaml\n{str(key)[2:-1]}```"
                        text = f"```yaml\n{str(text)[2:-1]}```"
                        etext = f"```yaml\n{etext}```"

                        embed = Embed(title="KeyViz Encryption", color=0xFF9999)
                        embed.add_field(name="Key", value=key, inline=False)
                        embed.add_field(name="Plain Text", value=text, inline=False)
                        embed.add_field(name="Encrypted Text", value=etext, inline=False)
                        await ctx.send(embed=embed)
                    except:
                        await ctx.send("Invalid key")
                else:
                    await ctx.send("Text is limited to 500 characters")
            else:
                await ctx.send("You can't just send a key, you need text too!")
        else:
            await ctx.send("You haven't specified anything to encrypt!")

    @commands.command(name="decrypt")
    async def _decrypt(self, ctx, *args):

        await ctx.channel.trigger_typing()

        if args:
            args = list(args)
            key = bytes(args[0], encoding="utf_8")
            args.pop(0)                    
            if args:
                etext = " ".join(args)
                if len(etext) <= 1000:
                    lock = Fernet(key)
                    etext = bytes(etext, encoding="utf_8")
                    try:
                        text = str(lock.decrypt(etext))[2:-1]

                        key = f"```yaml\n{str(key)[2:-1]}```"
                        etext = f"```yaml\n{str(etext)[2:-1]}```"
                        text = f"```yaml\n{text}```"

                        embed = Embed(title="KeyViz Decryption", color=0xFF9999)
                        embed.add_field(name="Key", value=key, inline=False)
                        embed.add_field(name="Encrypted Text", value=etext, inline=False)
                        embed.add_field(name="Plain Text", value=text, inline=False)
                        await ctx.send(embed=embed)
                    except:
                        await ctx.send("Invalid key/text")
                else:
                    await ctx.send("Text is limited to 1000 characters")
            else:
                await ctx.send("You haven't specified anything to decrypt!")
        else:
            await ctx.send("You haven't specified the key!")

def setup(bot):
    bot.add_cog(encryption(bot))
