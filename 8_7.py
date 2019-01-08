def make_album(singer, name, number='3') :
	album = {"singer":singer, "name":name, "number":number}
	return album
album1 = make_album("周杰伦", "七里香")
album2 = make_album("许嵩", "大千世界", "6")
print(album1)
print(album2)