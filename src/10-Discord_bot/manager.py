from discord.ext import commands
from discord.ext.commands.errors import MissingRequiredArgument, CommandNotFound

class Manager(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Estou conectado como {self.bot.user}")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("Mande todos os argumentos")
        elif isinstance(error, CommandNotFound):
            await ctx.send("O comando não existe. Digite !help para saber os comandos")
        else:
            raise error
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.name == self.bot.user.name:
            return
        print(f'{message.author.name} mandou mensagem no canal {message.channel.name}')

        if 'palavrão' in message.content:
            await message.channel.send(f'Por favor, {message.author}, não ofenda os demais usuários!')
            await message.delete()

        await self.bot.process_commands(message)

def setup(bot):
    bot.add_cog(Manager(bot))