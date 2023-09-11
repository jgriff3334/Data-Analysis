#Make full list and empty list

sandwich_orders = ['italian', 'pastrami','turkey club', 'cuban','pastrami', 'reuben', 'pastrami','ham and cheese', 'blt']
finished_sandwiches = []

#add message: out of pastrami
print("I'm sorry, but we are out of pastrami.")

while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

#Set loop

while sandwich_orders:
	order = sandwich_orders.pop()
	
	print("I made the " + order + " sandwich.")
	finished_sandwiches.append(order)
	
#print message that each sandwich was made
print("\nI made the following sandwiches:")
for sandwich in finished_sandwiches:
	print(sandwich)
