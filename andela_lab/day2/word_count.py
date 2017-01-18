def words_count(my_word):
	
		my_dict ={}
		
		unique_word = my_word.split()
		#the loop picks all the unique words in list
		for word in unique_word:
			count = 0
			
			for n in my_word.split():
				#compare the loop variables
				
				if word  == n:
					count = count + 1
					
					if word.isdigit() == True:
							word = int(word)
							
			my_dict[word] = count
	

		return my_dict

