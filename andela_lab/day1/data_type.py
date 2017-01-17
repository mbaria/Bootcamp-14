def data_type(n):
	
	n_type =type(n)
	if n_type == str:
		return len(n)
	elif n_type ==bool:
		return n
	elif n_type ==int:
		if n == 100:
			return 'equal to 100'
		elif n < 100:
			return 'less than 100'

		else:
			return 'more than 100'

	elif n_type ==list:
		try:
			if n[2]:
				return n[2]
		except(IndexError):
			return None
	else:
		return 'no value'