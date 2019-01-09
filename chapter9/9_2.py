class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
	
	def describe_restaurant(self):
		print(self.restaurant_name)
		print(self.cuisine_type)
	
	def open_restaurant(self):
		print("Restaurant is working")

restaurant_1 = Restaurant('McDonald', 'fast_food')
restaurant_2 = Restaurant('同福客栈', '打烊了')
restaurant_3 = Restaurant('四川烧烤', 'Babicu')
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()