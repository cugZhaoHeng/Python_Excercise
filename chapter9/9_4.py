class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0
	
	def describe_restaurant(self):
		print(self.restaurant_name)
		print(self.cuisine_type)
	
	def open_restaurant(self):
		print("Restaurant is working")
	
	def set_number_served(self, number_served):
		self.number_served = number_served
	
	def increment_number_served(self, number_served):
		self.number_served += number_served
	
restaurant_1 = Restaurant("同福客栈", "李大嘴")
print("The number of served is " + str(restaurant_1.number_served) + ".")
restaurant_1.set_number_served(7)
for i in range(1,5):
	restaurant_1.increment_number_served(3)
print("The number of served is " + str(restaurant_1.number_served) + ".")