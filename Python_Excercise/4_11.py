my_pizzaes = ["apple pizza", "new aulan", "chese"]
friend_pizzaes = my_pizzaes[:]
my_pizzaes.append("orange pizza")
friend_pizzaes.append("banana pizza")
print("My favorite pizza are:")
for my_pizza in my_pizzaes :
	print(my_pizza)
print("My friends favorite pizza are:")
for friend_pizza in friend_pizzaes :
	print(friend_pizza)
