class BinarySearch(list):
	

		def __init__(self, a, b):
			super(BinarySearch, self).__init__(range(b, a*b + b,b))
			self.length = a
	

		def search(self, target):
			bool_find, elem_idx, count = binary_search(target, self)
			out_put = {}
			out_put['count'] = count
			out_put['index'] = elem_idx
	

			return out_put
	

	def binary_search(val, alist):
		
		alist.sort()	
		
		sub_list = alist
		n = 0
	

		if val == sub_list[0] or val == sub_list[-1]:
			return True, alist.index(val), n
	

		while sub_list:
			stat = 0
			stop = len(sub_list) - 1
			mid = int(round((stat + stop)/2))
			n += 1
			
			if out_of_range(val, sub_list):
				if sub_list[0] > val or sub_list[-1] < val:
					n += 2
					return False, -1, n
			else:
				if val == sub_list[mid]:
					return True, alist.index(val), n
				elif val < sub_list[mid]:
					sub_list = sub_list[ : mid]				
				else:
					stat = mid + 1
					sub_list = sub_list[stat :]
	

	

	def out_of_range(t, l):
		if l[0] > t or l[-1] < t :
			return True
		else:
			return False

