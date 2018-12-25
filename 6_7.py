# 创建若干个字典，存放用户信息
duwei = {"first_name" : "Du", "last_name" : "Wei", "age" : 24, "city" : "Wuhan"}
kaifang = {"first_name" : "Gu", "last_name" : "Kaifang", "age" : 26, "city" : "Xinxiang"}
jinliang = {"first_name" : "Ma", "last_name" : "Jinliang", "age" : 26, "city" : "Siping"}
tianbo = {"first_name" : "Tian", "last_name" : "Bo", "age" : 24, "city" : "Qianjiang"}

# 将字典存放到列表中
users = [duwei, kaifang, jinliang, tianbo]

# 遍历此列表，打印其中的信息
for user in users :
	print("Name: "+user["first_name"]+" "+user["last_name"])
	print("Age: "+ str(user["age"]))
	print("City: "+str(user["city"]+"\n"))
