#First way to import function:

#import eight_pizza

#eight_pizza.make_pizza(16, 'pepperoni')
#eight_pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#Second way to import function:

#from eight_pizza import make_pizza

#make_pizza(16, 'pepperoni')
#make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#Third way to import function:

from eight_pizza import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
