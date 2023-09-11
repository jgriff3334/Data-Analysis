alien = "green"
if alien == "green":
	print("Congratulations! You earned 5 points!")

if alien == "yellow":
	print("Congratulations! You earned 5 points!")
	
alien = "red"
if alien == "green":
	points = 5
elif alien == "yellow":
	points = 10
elif alien == "red":
	points = 15
print("Congratulations! You just earned " + str(points) + " points!")
