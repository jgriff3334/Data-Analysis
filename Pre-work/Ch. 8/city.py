#def describe_city(city_name, city_country = 'USA'):
#	"""State the name of a city and where it is located."""
#	print(city_name.title() + " is located in " + city_country + ".")
#describe_city('austin')
#describe_city('denver')
#describe_city('london')

def city_country(city_name, country_name):
	"""Returns a city and it's country,"""
	print(city_name.title() + ", " + country_name.title())
city_country('dublin','ireland')
city_country('london','england')
city_country('new york city','united states')
