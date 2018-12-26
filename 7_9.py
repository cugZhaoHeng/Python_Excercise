sandwich_orders = ['牛肉', 'pastrami','羊肉','pastrami', '猪肉', 'pastrami']
print(sandwich_orders)
finished_sandwich = []
print("Sorry, pastrami have been saled")
while 'pastrami' in sandwich_orders :
	sandwich_orders.remove("pastrami")
while sandwich_orders : 
	sandwich = sandwich_orders.pop()
	print("I made your " + sandwich + " sandwich")
	finished_sandwich.append(sandwich)
for sandwich in finished_sandwich :
	print(sandwich)

