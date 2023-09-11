#message = "What kind of car would you like to rent?"

#name = input(message)
#print("Let me find a " + name + " for you.")



#number_group = input("How many people are in your group?" )
#number_group = int(number_group)

#if number_group > 8:
#	print("It will be a ten minute wait for a table.")
#else:
#	print("Right this way. We can seat you now.")


number = input("Give me a number and I'll tell you if it is a multiple of ten.")
number = int(number)

if number % 10 == 0:
	print("This is a multiple of ten.")
else:
	print("This number is not a multiple of ten.")
	
