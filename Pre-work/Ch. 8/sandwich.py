def make_sandwich(*ingredients):
	"""List the ingredients in a sandwich being ordered."""
	print("\nCan I please order a sandwich with the following?")
	for ingredient in ingredients:
		print("~" + ingredient)
make_sandwich('turkey', 'swiss')
make_sandwich('bacon', 'lettuce', 'tomato', 'mayo')
make_sandwich('hummus', 'peppers', 'onion')
