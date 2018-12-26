sandwich_orders = ['牛肉', '羊肉', '猪肉']
finished_sandwich = []
while sandwich_orders : 
	sandwich = sandwich_orders.pop()
	print("I made your " + sandwich + " sandwich")
	finished_sandwich.append(sandwich)
for sandwich in finished_sandwich :
	print(sandwich)