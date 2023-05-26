from discord.ext import commands

class Reactions(commands.Cog):
    """ Fala com o usuario """

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        print(reaction.emoji)
        if reaction.emoji == "👍":
            role = user.guild.get_role(1111364000438046792)
            await user.add_roles(role)
        elif reaction.emoji == "🐴":
            role = user.guild.get_role(1111363956037132369)
            await user.add_roles(role)

def setup(bot):
    bot.add_cog(Reactions(bot))