def make_album(artist_name, album_title, tracks=""):
	"""Return the artist name and album title in a dictionary."""
	album = {'artist': artist_name, 'album': album_title}
	return album
#	if tracks:
#		album['tracks'] = tracks
#	return album
#record = make_album('adele','30')
#print(record)
#record = make_album('justin timberlake','the 20/20 experience')
#print(record)
#record = make_album('paramore','riot',tracks = 12)
#print(record)
while True:
	print("\nPlease tell me the artist and album.")
	print("\n(Type 'q' to quit at any time.)")
	a_name = input('Artist name:')
	if a_name == 'q':
		break
	al_name = input('Album name:')
	if al_name == 'q':
		break
	record = make_album(a_name, al_name)
	print(record)
