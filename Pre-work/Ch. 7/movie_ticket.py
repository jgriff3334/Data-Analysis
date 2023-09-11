#writing simple script for age and ticket prices
age = input("\nHow old are you?")
#age += "\n(Enter quit when you are finished.)"
age = int(age)

while True:
	if age < 3:
		print("Your ticket is free!")
	elif age <= 12:
		print("Your ticket is $10.")
	elif age > 12:
		print("Your ticket is $15.")
		break
	
