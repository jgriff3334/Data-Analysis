def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user."""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile
	
#user_profile = build_profile('albert', 'einstein',
							#location = 'princeton',
							#field = 'physics')
user_profile = build_profile('jenni', 'griffin', location = 'florida', 
								hair_color = 'red',
								eye_color = 'blue')
print(user_profile)
