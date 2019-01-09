def make_great(magicians):
	'''给列表每个元素之前添加字符串 the great '''
	#for magician in magicians:
	#	magician = "the Great "+magician
	for index in range(len(magicians)):
		magicians[index] = "the great " + magicians[index]

def show_magicians(magicians):
	'''遍历并打印列表'''
	for magician in magicians:
		print(magician)
		
magicians_name = ['Jobs', 'Jack Ma', 'Liu', 'Tomas']
make_great(magicians_name)
show_magicians(magicians_name)
