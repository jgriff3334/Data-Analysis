def show_magicians(names):
	"""Display magician's names."""
	for name in names:
		print(name.title())
#magicians = ['houdini', 'david copperfield', 'david blaine']
show_magicians(magicians)

magicians = ['houdini', 'david copperfield', 'david blaine']
great_magicians = []
def make_great(great_magicians):
	"""add 'the Great' to each name"""
	while magicians:
		current_magicians = magicians.pop() + ' the Great'
		print(current_magicians.title())
		great_magicians.append(current_magicians)
make_great(great_magicians)

		
		
