prompt = "\nPlease tell me what toppings you want on your pizza."
prompt += "\n(Enter quit when you are finished.)"

while True:
	topping = input(prompt)
	
	if topping == "quit":
		break
	else:
		print("Adding " + topping + " to your pizza.")
	
