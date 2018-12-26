def make_shirt(size, word) :
	''' 打印衬衫的尺寸和样式'''
	print("This shirt's size is " + size + " and word is " + word)
# 使用位置实参
make_shirt("large", "Change the world")
# 使用关键字实参
make_shirt(size="middle", word="Commit and push")