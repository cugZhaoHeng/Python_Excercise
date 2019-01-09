class User():
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.login_attempts = 0
		
	def increment_login_attempts(self):
		self.login_attempts += 1
		
	def reset_login_attempts(self):
		self.login_attempts = 0

		
user_1 = User("Gu", "Kai Fang")
for i in range(1, 5):
	user_1.increment_login_attempts()
print(user_1.login_attempts)
user_1.reset_login_attempts()
print(user_1.login_attempts)