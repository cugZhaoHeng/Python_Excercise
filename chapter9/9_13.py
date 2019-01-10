from collections import OrderedDict

word_code = OrderedDict()
word_code['Java'] = 'A strong program language'
word_code['PHP'] = 'The best language'
word_code['C++'] = 'Objected labguage'
for key, value in word_code.items():
	print(key+' '+value)
