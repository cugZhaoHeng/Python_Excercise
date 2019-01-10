filename='python_learn.txt'

with open(filename) as file_object:
	lines=file_object.readlines()
	contents=file_object.read()
	

print(contents)

for line in lines:
	print(line)
