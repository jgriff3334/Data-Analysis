pizzas = ['mushroom', 'pepperoni', 'veggie', 'sausage', 'buffalo chicken']
friends_pizzas = ['mushroom', 'pepperoni', 'veggie', 'sausage', 'buffalo chicken']
pizzas.append('hawaiian')
friends_pizzas.append('margherita')
print(pizzas)
print(friends_pizzas)
print("My favorite pizzas are:")
for pizza in pizzas:
	print(pizza.title())
print("My friend's favorite pizzas are:")
for friend in friends_pizzas:
	print(friend.title())
