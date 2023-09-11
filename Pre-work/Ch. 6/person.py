#person_0 = {'first_name': 'steven', 'last_name': 'siemienski', 'city': 'philadelphia'}
#person_1 = {'first_name': 'aaron', 'last_name': 'cain', 'city': 'niceville'}
#person_2 = {'first_name': 'leah', 'last_name': 'hill', 'city': 'nashville'}

#people = [person_0, person_1, person_2]

#for person in people:
#	print(person)

#print(person['first_name'].title() + " " + person['last_name'].title() +
#	" is from " + person['city'].title())

numbers = {
	'aaron': [33, 22],
	'lydia': [14],
	'olivia': [23, 5, 17],
	'bryna': [2],
	'charles': [34, 23],
	'parker': [4],	
	}
for name, favorite in numbers.items():
	print("\n" + name.title() + "'s favorite number(s) are:")
	for fave in favorite:
		print(str(fave))
#print("Aaron's favorite number is " + str(numbers['aaron']) + ".")
#print("Lydia's favorite number is " + str(numbers['lydia']) + ".")
#print("Olivia's favorite number is " + str(numbers['olivia']) + ".")
#print("Bryna's favorite number is " + str(numbers['bryna']) + ".")
#print("Charles' favorite number is " + str(numbers['charles']) + ".")
#print("Parker's favorite number is " + str(numbers['parker']) + ".")

#glossary = {
#	'variable': 'holds a value',
#	'string': 'Anything inside quotations',
#	'method': 'An action that can be performed on a piece of data',
#	'concatenation': 'Combining strings with a + symbol',
#	'syntax_error': 'Indicates that the interpreter does not recognize something within the code',
#	'set': 'Pulls out the unique items',
#	'dictionary' : 'A collection of key-value pairs',
#	'key-value pair' : 'A set of values associated with each other',
#	'PEP' : 'Python enhancement proposal; PEP 8 teaches how to style code',
#	'tuple': 'An immutable list'
#	}
#for word, definition in glossary.items():
#	print(word.title()+ ": " + definition)


