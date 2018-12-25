active = True
while active :
	age = input("Please enter a age: ")
	if age == "exit" :
		active = False;
	else :
		age = int(age)
		if age < 3 and age > 0 :
			print("It's free")
		elif age >= 3 and age < 12 :
			print("The price is 10 dollars")
		elif age >= 12 :
			print("The price is 15 dollars")