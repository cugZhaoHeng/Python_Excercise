visit_post = {}
active = True
while active :
	name = input("Please enter your name: ")
	place = input("Please tell me where would you want to visit: ")
	visit_post[name] = place
	flag = input("Continue?yes/no: ")
	if flag == "no" :
		active = False
	else :
		active = True
for name, place in visit_post.items() :
	print(name + "想去" + place)
	