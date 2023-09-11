favorite_places = {
	'jenni':['hawaii', 'grand canyon', 'ireland'],
	'april':['italy'],
	'leah':['england', 'scotland'],
	}
for name, places in favorite_places.items():
	print("\n" + name.title() + "'s favorite places are:")
	for place in places:
		print(place.title())
