from user import User
from privileges import Privileges

class Admin(User):
	def __init__(self, first_name, last_name):
		super().__init__(first_name, last_name)
		self.privileges = Privileges(['add', 'delete'])
		
	
		
admin_1 = Admin('zhang', 'san')
admin_1.privileges.show_privileges()