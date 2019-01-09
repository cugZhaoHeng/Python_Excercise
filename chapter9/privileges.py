class Privileges():
	def __init__(self, privileges=['add post', 'delete post', 'ban user']):
		self.privileges = privileges
		
	def show_privileges(self):
		print(self.privileges)