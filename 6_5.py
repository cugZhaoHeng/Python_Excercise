rivers = {"nile" : "egypt", "huangge" : "china", "misisibi" : "america"}

for river, country in rivers.items() :
	print("The " + river.title() + " runs through " + country.title())

print("========================")
for river in rivers.keys() :
	print(river)
print("=======================")
for country in rivers.values() :
	print(country)