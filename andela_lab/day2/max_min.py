def find_max_min(mylist):
	mylist.sort()
	if mylist[0] == mylist[-1]:
		return [len(mylist)]
	else:
		return [mylist[0], mylist[-1]]