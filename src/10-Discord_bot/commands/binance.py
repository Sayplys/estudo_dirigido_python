from discord.ext import commands
import requests

class Binance(commands.Cog):
    """ Fala com o usuario """

    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="moeda", help="Mostra cotações de acordo com os dados da binance (!moeda xxx xxx)")
    async def binance(self, ctx, coin, base):
        try:
            response = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}{base.upper()}")
            data = response.json()
            price = data.get("price")

            if price:
                await ctx.send(f"O valor do par {coin}/{base} é {price}")
            else:
                await ctx.send(f"O valor do par {coin}/{base} é invalido")
        except Exception as error:
            await ctx.send("Deu errado sua requisição")
            print(error)       

def setup(bot):
    bot.add_cog(Binance(bot))