# 创建宠物字典
cat = {"name" : "ameko", "host" : "xiamu"}
dog = {"name" : "inuyasha", "host" : "cakome"}

# 将字典存储到列表中
pets = [cat, dog]

# 打印字典信息
for pet in pets :
	for name, host in pet.items() :
		print(host + " is " + name + " 's host")