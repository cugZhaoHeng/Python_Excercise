def get_car(agent, type, **carinfo):
	car = {}
	car['agent']=agent
	car['type']=type
	for key, value in carinfo.items():
		car[key]=value
	return car

car = get_car('subaru', 'outback', color='blur', tow_package=True)
print(car)