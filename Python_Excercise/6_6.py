favorite_language = {
	'jen' : 'python',
	'sarah' : 'c',
	'john' : 'c++',
	'jack' : 'java'
	}
users = ['jack', 'jamson', 'jen', 'king']

for user in users :
	if user in favorite_language.keys() :
		print("Thanks for your application, " + user)
	else :
		print(user + ", please part in.")