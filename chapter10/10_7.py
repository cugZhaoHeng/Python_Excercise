def add_two_number():
	while True:
		try:
			number1 = int(input('enter first number: '))
		except ValueError:
			print('Please enter correct number!')
			continue
		else :
			break
	
	while True:
		
		try:
			number2 = int(input('enter second number: '))
		except ValueError:
			print('Please enter correct number!')
			continue
		else :
			break
	print(number1+number2)

add_two_number()
