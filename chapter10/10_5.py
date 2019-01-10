filename='love_reason.txt'

with open(filename, 'a') as file_object:
	while True:
		reason=input('Why you like code: ')
		if reason=='exit':
			break
		file_object.write(reason+'\t')
