#user_names = ['admin', 'jj234', 'kittycat','killertom','mightmouse','iluvsnacks']
#if user_names:
#	for user_name in user_names:
#		print("Hello " + user_name + ", welcome back!")
#else:
#	print("We need to add some users!")
current_users = ['sillygoose', 'goldenfleece', 'cherry', 'sammygurl', 'pinguino']
new_users = ['SILLYGOOSE', 'tweetybird', 'cherry', 'sadiehawkins', 'stawkward']
for new_user in new_users:
	if new_user.lower() in current_users:
		print("Username already in use. Please choose another.")
	else:
		print("This username is available. Continue?")
		
	
