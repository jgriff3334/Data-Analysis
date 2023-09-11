def make_shirt(shirt_size = 'large', shirt_text = 'I Love Python'):
	"""Display the size and the message on the shirt."""
	print("This order is for a size " + shirt_size + 
		" shirt with the phrase " + shirt_text + " on it.")
#shirt('small', '"howdy"')
#make_shirt(shirt_text = '"howdy"', shirt_size = 'small')
make_shirt()
make_shirt('medium')
make_shirt('small')
