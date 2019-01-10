def add_two_number():
	'''计算两个数值的和'''
	try:
		num1=int(input('enter first number: '))
		num2=int(input('enter second number: '))
	except (ValueError, TypeError):
		print('Please enter a integer number!')
	else:
		print(num1+num2)

add_two_number()
