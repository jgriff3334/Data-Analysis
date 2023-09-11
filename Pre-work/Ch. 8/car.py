def build_car(make, model, **options):
	"""Store information about a car in a dictionary."""
	car = {}
	car['make'] = make
	car['model'] = model
	for key, value in options.items():
		car[key] = value
	return car

car = build_car('toyota', 'corolla', year = '1998', color = 'navy',
				cd_player = True)
print(car)
