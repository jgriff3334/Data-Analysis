responses = {}

#Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
	#Prompt for the person's name and response.
	name = input("\nWhat is your name?")
	response = input("If you could visit anywhere, where would you go?")

	#Store the responses in a dictionary.
	responses[name] = response

	#Find out if anyone else is going to take the poll.
	repeat = input("Would you like to let another person respon? (yes/no) ")
	if repeat == 'no':
		polling_active = False
	
#Polling is complete. Show the results.
print("\n---Poll Results---")
for name, response in responses.items():
	print(name + " would like to visit " + response + ".")
