def make_album(singer, name, number="4") :
	album = {"singer":singer, "name":name, "number":number}
	return album
while(True) :
	print("If you want exit, please enter 'exit' in time")
	name = input("Please enter a name: ")
	if(name=="exit") :
		break;
	singer = input("Please enter a singer: ")
	if(singer == "exit") :
		break;
	number = input("Please enter a number: ")
	if(number == "exit") :
		break;
	album = make_album(singer, name, number)
	print("The album is "+album['name'] + album['singer'] + album['number'])