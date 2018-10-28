pizzas = ['Marinara', 'Romana', 'Contadina']
friend_pizzas = pizzas[:]
pizzas.append('bianche')
friend_pizzas.append('Prosciutto')
print('My favorite pizzas are:')
for pizza in pizzas:
    print(pizza)
print('My friend\'s favourite pizzas are')
for pizza in friend_pizzas:
    print(pizza)