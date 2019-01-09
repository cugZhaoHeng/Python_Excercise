from restaurant import Restaurant

class IceCreamStand(Restaurant):
	def __init__(self, restaurant_name, cuisine_type):
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = "草莓味"
		
	def show_ice_cream(self):
		print(self.restaurant_name+" " + self.cuisine_type+" "+self.flavors)
ice_cream_stand_1 = IceCreamStand("肯德基", "油炸")
ice_cream_stand_1.show_ice_cream()
