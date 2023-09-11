cities = {
	'philadelphia':{
		'country': 'united states',
		'population': 1603797,
		'fact': 'it is the largest city in Pennsylvania.',
		},
	'dublin':{
		'country': 'ireland',
		'population': 553000,
		'fact': 'it was the most important Viking town in Ireland.',
		},
	'munich':{
		'country': 'germany',
		'population': 1407000,
		'fact': 'it is the 3rd biggest city of Germany.',
		},
	}
for city, city_info in cities.items():
	print("\nCity: " + city.title())
	population = city_info['population']
	fact = city_info['fact']
	
	print("Population: " + str(population))
	print("A fact about this city is: " + fact)
	
