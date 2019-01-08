def build_profile(first, last, **userinfo):
	user = {}
	user['first'] = first
	user['last'] = last
	for key, value in userinfo.items():
		user[key] = value
	return user
	
user = build_profile(first='zhang', last='san', age=11, city='Wuhan')
print(user)