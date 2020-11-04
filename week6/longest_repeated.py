from pathlib import Path
import sys
#Part C
#1
def read_file(file):
	str_as_list=[]
	with open(file, 'r') as my_file:
		for line in my_file.readlines():
			str_as_list.append(line.strip().split(' '))  # remove new line character and split with space
	return str_as_list[:100]  # return the first n lines
#2
def bi_to_n_gram(n, input_text):
	count_n_grams = {}
	while(n > 1):   # it will start from counting grams from 2
		for s in input_text:
			for i in range(len(s)-n-1):
				key = tuple(s[i:i+n])
				if key in count_n_grams:
					count_n_grams[key]+=1 # if the key is there, the count value will increament by 1
				else:
					count_n_grams[key]=1
		n-=1
	return count_n_grams
#3
def ngr_counts(bi_to_n_gram):
	all_repeats = []    # used to hold all repeated values
	longest_repeated_gram = [] # used store the longest repeated grams
	for rep in bi_to_n_gram:
		if bi_to_n_gram[rep] > 1:
			all_repeats.append(rep)
	first_value = all_repeats[0]  # holds the first most repeated value
	for value in all_repeats:
		if len(value) == len(first_value):
			longest_repeated_gram.append(value)
	return longest_repeated_gram
def find_longest_repeat(n):
	result1 = ngr_counts(bi_to_n_gram(n, read_file(sys.argv[1])))
	n+=5
	result2 = ngr_counts(bi_to_n_gram(n, read_file(sys.argv[1])))
	while len(result1[0]) < len(result2[0]):  # for every increament value of n by 5, check the length of the result
		result1 = result2                    
		n+=5
		result2 = ngr_counts(bi_to_n_gram(n, read_file(sys.argv[1])))
	return result1  # returns result1 if the while condition terminates

def main():
	print(read_file(sys.argv[1]))      #1
	print(bi_to_n_gram(3, read_file(sys.argv[1]))) #2
	print(ngr_counts(bi_to_n_gram(10, read_file(sys.argv[1])))) #3
	print(find_longest_repeat(5)) #4

if __name__ == '__main__':
 	main()