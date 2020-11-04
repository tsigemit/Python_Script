''' Part C
============================================================================================================================= 
Styx
If you are given three sticks, you may or may not be able to arrange them in a triangle.
For example, if one of the sticks is 12 inches long and the other two are one inch long, 
you will not be able to get the short sticks to meet in the middle. For any three lengths, there is a simple test 
to see if it is possible to form a triangle: If any of the three lengths is greater than the sum of the other two,
then you cannot form a triangle. Otherwise, you can. (If the sum of two lengths equals the third, they form what is called a
“degenerate” triangle.)
Write a program which takes lengths of three sticks as keyboard input and then prints either “Yes” or “No”, 
depending on whether you can or cannot form a triangle from sticks with the entered lengths. (From Think Python.) '''
	
# to use for reduce
import functools 

len_stick1 = int(input("Enter lengths of stick1 "))
len_stick2 = int(input("Enter lengths of stick2 "))
len_stick3 = int(input("Enter lengths of stick3 "))

if len_stick1 > len_stick2+len_stick3 or len_stick2 > len_stick1+len_stick3 or len_stick3 > len_stick1+len_stick2:
    print("No")
elif len_stick1 == len_stick2+len_stick3 or len_stick2 == len_stick1+len_stick3 or len_stick3 == len_stick1+len_stick2:
	print("They form a degenerate triangle")
else:
	print("Yes")


'''Part D
  Map, reduce, filter, rinse & repeat

  1) Write programs to solve the tasks below. Where appropriate, use the templates for map, filter and reduce given in the 
  lecture. Some of the tasks rely on each other: If you cannot solve a task because you got stuck on a previous one, 
  try to give a short reply in prose of how you think one could solve that task.'''

# for this problem, I prefer to use filter. 
input_string = ['t', 'h', 'e', ' ', 'r', 'a', 'i', 'n', ' ', 'i', 'n', ' ', 's', 'p', 'a', 'i', 'n']
input_string = ['t', 'h', 'e', ' ', 'r', 'a', 'i', 'n', ' ', 'i', 'n', ' ', 's', 'p', 'a', 'i', 'n']
vowels = 'euiaoy'
output_list =[]
# I prefer to use a function so that I can reuse later
def list_vowels(input_values):
	list(filter(lambda c: output_list.append(1) if c in vowels else output_list.append(0), input_values))

list_vowels(input_string)
print(output_list)

'''2) For a list of numbers, we want to get the sum of the items.
 So input [10,20,30,40] should give 100. Again, what kind of operation is this? Write 
the code. (For the sake of this assignment, pretend the built-in sum function wasn't available.)'''

# I prefer to use reduce.
input_list = [10,20,30,40]
print(functools.reduce(lambda v1, v2: v1+v2, input_list))

'''
 3) If we put these two loops in a row and take the output of 1 as the input of 2, we have a way of counting the number of
 vowels in a string. Try it out! Maybe you have also noticed that it is possible to merge the two steps into one. Rewrite 
 your code so that you get one loop that takes a list of characters and calculates the number of vowels. 
 Is this a map, reduce or filter? Does the input have to be a list of characters or does it work with input of
 another type as well? If so, which ones?
 '''

 # we can use the reduce function to count the number of vowels in a list of char sequences
 # this can also be works with strings as strings are sequence of characters

print("Using reduce", functools.reduce(lambda v1, v2: v1+v2, output_list))

#using for loop to calculates the number of vowels in a list of char sequences. e.g for the input_string we define above
# I prefer to implement using a function to reuse on question number 4.
def count_vowels_using_for_loop(input_string):
	count_vowels = 0
	for c in input_string:
		if c in vowels:
			count_vowels += 1
	return count_vowels
print("Using for loop", count_vowels_using_for_loop(input_string))

'''
4) 
Using your solution for 3 and the map template, write code that maps a list of strings to a list where each item is the number of vowels
that the corresponding string contains. So ['the','rain','in','spain'] 
should give [1,2,1,2] and ['mainly','in','the','plain'] gives [3,1,1,2]/code>.
'''

intput_string_list = ['mainly','in','the','plain']

output_map = list(map(count_vowels_using_for_loop, intput_string_list))
print(output_map)

'''
5) 
Write a filter that takes a sequence of integers and only collects those integers that are divisible by 5 or by 7, 
but not by both. So for the input [14,30,35] the result should be [14,30], 
and for range(931,960) we should get [931, 935, 938, 940, 950, 952, 955, 959]. 
You can check divisibility by checking whether the remainder would be 0.
'''
find_divisibile1 = [14,30,35]
find_divisibile2 = range(931, 960)

print("divisible by 5 or 7=", list(filter(lambda x: (x%5 ==0 or x%7==0) and not (x%5==0 and x%7==0) , find_divisibile1)))
print("divisible by 5 or 7=", list(filter(lambda x: (x%5 ==0 or x%7==0) and not (x%5==0 and x%7==0) , find_divisibile2)))

'''
Below is an unrolled while-loop: 
'''
s = [1,5,10,4]
t = []
i = 0
# # enter the while loop
# t = [s[i]]+t
# i = i+1 # == 1
# t = [s[i]]+t
# i = i+1 # == 2
# t = [s[i]]+t
# i = i+1 # == 3
# t = [s[i]]+t
# i = i+1 # == 4
# exit the while loop
# solution using while loop
print("Using while loop")
while i in range(len(s)):
	  t = [s[i]]+t
	  i+=1
print(s)
print(t)

# 7) Rewrite your solution for 6 as a for-loop.
#    solution using for loop

print("Using for loop")
t=[]
for i in range(len(s)):
	t = [s[i]]+t
print(s)
print(t)

#Part E
# I prefered to implement this using function as follows.
# The function arguments are the whole_deck and the card we want to search. 
# The while loop becomes False 
# 1) If bottom is greater than top. This if the card we want search is less than all the cards and not on our 
# cards, elif my_card < whole_deck[middle]: is always True and value of top is decearmented by 1. Then at some point value of top becoms -1
# and the while loop will break and the conde print("Card can't be found") is excuted.
# 2) if the my_card is greater than all the whole_deck values, bottom will increment every time
# and it will reach bottom == top = len(whole_deck), the while loop will becomes False and breads out of while loop
def find_card(whole_deck, my_card):
	top = len(whole_deck)
	bottom = 0
	while bottom <= top and bottom < len(whole_deck):
		middle = (top+bottom)//2
		if whole_deck[middle] == my_card:
			print('Card', my_card, 'is at position', middle)
			return
		elif my_card < whole_deck[middle]:
			top = middle-1; # search on the left half of whole_deck
		else:
			bottom = middle+1 # search on the right half of whole_deck
	print("Card can't be found") # if not found, this is excuted

whole_deck ="abcdefg"
my_card ='c'
print('Looking for card', my_card,'among', whole_deck)
find_card(whole_deck, my_card)


