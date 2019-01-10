def read_file(word, filename):
	try:
		with open(filename, encoding='utf-8') as file_object:
			contents = file_object.read()
	except FileNotFoundError:
		print('The file ' + filename + ' is not found')
	else:
		calculate_words(word, contents)
def calculate_words(word, contents):
	count = contents.lower().count(word)
	print('The "script" has '+str(count) + ' count')

word = 'script'
filename_1 = 'source.txt'
read_file(word, filename_1)

