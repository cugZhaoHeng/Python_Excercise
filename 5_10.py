current_users = ["DUwei", "KAIfang", "JINliang", "WANGyu", "TIANbo"]
# 使用列表解析快捷生成一个列表
current_users1 = [user1.lower() for user1 in current_users]
print(current_users1)
new_users = ["WENqian", "PENGyi", "jinliang", "kaifang", "YUxin"]

for user in new_users :
	if user.lower() in current_users1 :
		print(user + " was used.")
	else :
		print(user + " was not used.")