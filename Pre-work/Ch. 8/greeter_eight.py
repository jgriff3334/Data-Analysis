#def greet_user(username):
#	"""Display a simpple greeting."""
#	print("Hello!" + username.title() + "!")

#greet_user('jesse')

#def display_message():
#	"""Explain what you are learning."""
#	print("Chapter eight is teaching functions.")

#display_message()

#def favorite_book(book_name):
#	"""Display your favorite book."""
#	print("My favorite classic is " + book_name.title() + ".")
	
#favorite_book('jane eyre')

def get_formatted_name(first_name, last_name):
	"""Return a full name, neatly formatted."""
	full_name = first_name + " " + last_name
	return full_name.title()
# This is an infinite loop!
while True:
	print("\nPlease tell me your name:")
	print("(enter 'q' at any time to quit)")
	f_name =  input("First name:")
	if f_name == 'q':
		break
	l_name = input("Last name:")
	if l_name == 'q':
		break
	
	formatted_name = get_formatted_name(f_name, l_name)
	print("\nHello, " + formatted_name + "!")
