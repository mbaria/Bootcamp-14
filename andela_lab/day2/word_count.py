def words(phrase):
	#from collections import Counter
	list_words = phrase.split()
	temp_out = {}
	#temp_out = dict(Counter(list_words))
	for elem in list_words:
		if elem in temp_out:
			continue
		else:
			temp_out[elem] = list_words.count(elem)

	out = {}

	for item in temp_out.items():
		if item[0].isdigit():
			out[int(item[0])] = item[1]
		else:
			out[item[0]] = item[1]

	return out