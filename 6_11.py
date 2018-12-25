cities = {
	"Wuhan" : {"country" : "China", "population" : 4000000, "fact" : "hot"},
	"Beijing" : {"country" : "China", "population" : 10000000, "fact" : "cold"},
	"New_York" : {"country" : "USA", "population" : 3000000, "fact" : "rich"}
	}
for city, info in cities.items() :
	print(city + " is belong to " + info["country"] + ", and about " + str(info["population"]) + " and very" + info["fact"])
