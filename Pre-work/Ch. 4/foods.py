foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = foods[:]
foods.append('cannoli')
friends_foods.append('ice cream')
print("My favorite foods are:")
for food in foods:
	print(food)
print("\nMy friend's favorite foods are:")
for friend in friends_foods:
	print(friend)
