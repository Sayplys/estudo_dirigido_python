from discord.ext import commands, tasks
from discord import utils

class Dates(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @tasks.loop(minutes=15)
    async def current_time(self):
        now = utils.datetime.datetime.now()
        now = now.strftime('%d/%m/%Y as %H:%M:%S')

        channel = self.bot.get_channel(1110550193029533719)

        await channel.send("Data atual: " + now)

    
async def setup(bot):
    await bot.add_cog(Dates(bot))
    