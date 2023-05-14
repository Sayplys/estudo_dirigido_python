""" Aula 03 - *args e **kwargs """

# Args manda uma lista de argumentos
# sem keywords para ser usadas 
# como parâmetro em uma função
def world_cup_title(contry, *args):
    print('Contry: ', contry)
    for title in args:
        print('Year: ', title)

print(world_cup_title('Brazil', '1958', '1962', '1970', '1994','2002'))
print(world_cup_title('Espanha', 2010))


# Kwargs manda uma lista de argumentos
# com keywords para ser usadas 
# como parâmetro em uma função
def calculate_price(value, **kwargs):
    tax_percentage = kwargs.get('tax_percentage')
    discount = kwargs.get('discount')

    if tax_percentage:
        value += value * (tax_percentage / 100)
    if discount:
        value -= discount
    return value

print(calculate_price(1000))
print(calculate_price(1000, discount=4))
print(calculate_price(1000, tax_percentage=3))
print(calculate_price(1000, discount=10, tax_percentage=2))
