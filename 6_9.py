# 创建每个人所喜欢城市的字典，其中城市用列表存放
favorite_place = {
	"kaifang" : ["Xinjiang", "Zhengzhou", "Wuhan"],
	"jinliang" : ["Shenyang", "Siping", "Changchun"],
	"tianbo" : ["Wuhan"],
	"zhaoheng" : ["Wuhan", "Shenzhen"]
	}

# 遍历该字典
for name, places in favorite_place.items() :
	if len(places) == 0 :
		print(name.title + " does not have any favorite place.")
	elif len(places) == 1 :
		print("The " + name.title() +" favorite place is: " + places[0])
	else :
		print("The " + name.title() + " favorite places are: ")
		for place in places :
			print(place)
	print()
