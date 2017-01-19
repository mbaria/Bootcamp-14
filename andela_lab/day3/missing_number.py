def find_missing(list1,list2):
	
		absent = 0
		#find missing number if first list is smaller
		if len(list1) < len(list2):
			miss = (set(list2) - set(list1))
			absent = miss.pop()
			return absent
		#find missing number if second list is smaller
		if len(list2) < len(list1):
			miss = (set(list1) - set(list2))
			absent = miss.pop()
			return absent
		
		else:
		  return 0

