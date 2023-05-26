from discord.ext import commands
import re

class Calculator(commands.Cog):
    """ Fala com o usuario """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="calcular", help="Calculadora (!calcular x+(2-3)+4x9/2")
    async def calculate_expression(self, ctx, *message):
        expression = ''.join(message)
        numeros = re.split(r"[+ x / ( ) -]+", expression)
            
        signals_input = []
        for char in expression:
            if char == '+' or char == 'x' or char == '/' or char == '-' or char == '(' or char == ')':
                if char == 'x':
                    signals_input.append('*')
                    continue
                signals_input.append(char)

        math = ''

        for indice, numero in enumerate(numeros):
            try:
                int(numero)
                if indice < len(numeros) - 1:
                    if indice < len(numeros) - 2:
                        if signals_input[indice + 1] == '(':
                                math += f'{numero}{signals_input[indice]}('
                                signals_input.remove('(')
                        elif signals_input[indice] == ')':
                                math += f'{numero}){signals_input[indice + 1]}'
                                signals_input.remove(')')
                        else:
                                math += f'{numero}{signals_input[indice]}'
                    else:
                        math += f'{numero}{signals_input[indice]}'
                else:
                    math += f'{numero}'
            except ValueError:
                await ctx.send('Por favor, mande uma conta válida.')
                return
            
        response = eval(math)
        
        # response = eval(math)

        await ctx.send('A resposta é: ' +  str(response))



def setup(bot):
    bot.add_cog(Calculator(bot))