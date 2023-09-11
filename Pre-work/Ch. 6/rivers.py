rivers = {
	'amazon' : 'south america',
	'nile' : 'africa',
	'yangtze' : 'china',
	'mississippi' : 'north america',
	}
for river, location in rivers.items():
	print("The " + river.title() + " runs through " +
		location.title() + ".")
for river in rivers:
	print(river.title())
for location in rivers:
	print(location.title())
