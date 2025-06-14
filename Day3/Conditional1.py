print("Welcome to rollercoaster!")

height = int(input("What is your height in cm ?"))
age=int(input("Enter your age:"))

if height >=120:
	print("You can ride rollercoaster")
	if age <12:
		print("Your Ticket Cost is 5 dollar.")
	elif age <= 18 :
			print("Your Ticket Cost is 7 dollar.")
	else:
		print("Your Ticket Cost is 12 dollar.")
else:
	print("You have to grow taller before you can ride.")