def read_file(filename):
	try:
		with open(filename) as file_object:
			lines = file_object.readlines()
	except FileNotFoundError:
		pass
	else :
		for line in lines:
			print(line.rstrip())

filename_1 = 'cat.txt'
filename_2 = 'dog.txt'

read_file(filename_1)
read_file(filename_2)

