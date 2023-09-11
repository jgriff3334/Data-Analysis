big_cat = 'tiger'
print("Is big_cat == 'tiger'? I predict True.")
print(big_cat == 'tiger')

print("/Is big_cat == 'lion'? I predict False.")
print(big_cat == 'lion')


car = 'toyota'
print("Is the car == 'toyota'? I predict True.")
print(car == 'toyota')

print("Is the car == 'ford'? I predict False.")
print(car == 'ford')


veggie = 'carrot'
print("Is the veggie == 'carrot'? I predict True.")
print(veggie == 'carrot')

print("/Is the veggie == 'celery'? I predict False.")
print(veggie == 'celery')


fruit = 'strawberry'
print("Is the fruit == 'kiwi'? I predict False.")
print(fruit == 'kiwi')

print("/Is the fruit == 'strawberry'? I predict True.")
print(fruit == 'strawberry')


animal = 'cat'
print("Is the animal == 'dog'? I predict False.")
print(animal == 'dog')

print("/Is this animal == 'cat'? I predict True.")
print(animal == 'cat')

movie = 'Up'
print("Is movie == 'Up'? I predict True.")
print(movie == 'Up')

print("/Is movie == 'Saw'? I predict False.")
print(movie == 'Saw')

sport = 'soccer'
print("Is sport == 'baseball'? I predict False.")
print(sport == 'baseball')

print("/Is sport == 'soccer'? I predict True.")
print(sport == 'soccer')

game = 'proceed'
print("Is game == 'spades'? I predict False.")
print(game == 'spades')

print("/Is game == 'proceed'? I predict True.")
print(game == 'proceed')

name = 'steven'
print("Is his name == 'steven'? I predict True.")
print(name == 'steven')

print("/Is his name == 'dave'? I predict False.")
print(name == 'dave')

friend = 'leah'
print("Is friend == 'emily'? I predict False.")
print(friend == 'emily')

print("/Is friend == 'leah'? I predict True.")
print(friend == 'leah')

herb = 'rosemary'
if herb != 'organo':
	print("Yes! We do have that herb!")
	

age = 19
if age != 21:
	print("I'm sorry, but you cannot enter.")
	
age_1 = 20
age_2 = 22
age_1 >= 21 or age_2 >= 21
age_1 >= 18 and age_2 >= 18
age_1 >= 21 and age_2 >= 21

approved_users = ['katie', 'dave', 'jackson', 'millie']
user = 'james'
if user not in approved_users:
	print(user.title() + ", you do not have access to this section.")
user_2 = 'katie'
if user_2 in approved_users:
	print(user_2.title() + ", welcome back!") 
