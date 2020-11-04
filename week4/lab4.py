# #1
# first_last_name = (('Gerlof von', 'Bayes'), ('Anna', 'Lang'), ('Diderik', 'Legrand'), ('Pi', 'Thon-Rappel'))
# #2
# dic_of_children = {'4567':{'name':'Gerlof', 'date_of_birth': '2016-12-31'}, 
#                    '2345':{'name':'Anna', 'date_of_birth': '2015-08-14'}, 
#                    '0123': {'name':'Diderik', 'date_of_birth': '2015-03-03'}, 
#                    '8901':{'name':'Pi', 'date_of_birth': '2015-02-29'}
#                    }                         
# #3
# favorite_topic ={ '4567': {'name': 'Gerlof','topic': ['syntax', 'historical linguistics', 'logic programming','spelling']}, 
#                   '2345': {'name': 'Anna', 'topic':['argumentation analysis']}, 
#                   '0123':  {'name': 'Diderik','topic': ['NLP for Gothic']}, 
#                   '8901': {'name': 'Pi', 'topic': ['programming language design']}
#            }

#favorite_topic['0123']['topic']='sand castle engineering';

#4
child_information ={'4567':{"first_name": 'Gerlof',
                          "last_name": 'Bayes',
                          'date_of_birth': '2016-12-31',
                          "topic": ['syntax', 'historical linguistics', 'logic programming','spelling']
                          },

                    '2345':{"first_name":'Anna',
                          "last_name":'Lang',
                          'date_of_birth': '2015-08-14',
                          "topic":['argumentation analysis']
                          },

                    '0123':{"first_name": 'Diderik',
                          "last_name": 'Legrand',
                          'date_of_birth': '2015-03-03',
                          "topic":['NLP for Gothic'],
                          },
                    '8901':{"first_name": 'Pi',
                          "last_name": 'Thon-Rappel',
                          'date_of_birth': '2015-02-29',
                          "topic":['programming language design']
                          },

                          }
#5
# Here, we can use the string format function to format the output. 
#the numbers specifies how much space is required for that column.

print("Children Information")
print("====================")
print()
format_string = "{:10}  {:10}  {:10}"
headers = ['Soc.sec.no', 'Name ', 'Birthday'] 
header_rows = format_string.format(*headers)

print(header_rows)
print('-'*len(header_rows))

for id in child_information.keys():
	print(format_string.format(id, child_information[id]['first_name'], child_information[id]['date_of_birth']))

# To list children whose last name start with L
print()
print("children Information whose name starts with L")
print()
print(header_rows)
print('-'*len(header_rows))
for id in child_information.keys():
	if child_information[id]['last_name'].startswith('L'):
		print(format_string.format(id, child_information[id]['first_name'], child_information[id]['date_of_birth']))

#6
# to update Diderik birthday
child_information['0123']['birthday'] = '454-05-12'

# to remove Gerlof's interest from the topic spelling
child_information['4567']['topic'].remove('spelling')

#Part B, Counting bigrams

#1 
# the list of bigrams
print()
print("bigrams counts")
print("--------------")


list_bigrams= ['to','be',',','or','not','to','be',',','that','is','the','question',':']
count_bigrams = {} # a dictionary to hold bigram pairs with their respective counts

for i in range(len(list_bigrams)-1):
		key = tuple(list_bigrams[i:i+2])
		if key in count_bigrams:
			count_bigrams[key]+=1
		else:
			count_bigrams[key]=1
		

for item in count_bigrams.items():
	print(item)
#2 Using dictionary
bigrams_dict_of_dict={}
print()
print("bigrams counts using dictionary of dictionaries")
print("------------------------------------------------")
for key in count_bigrams.keys():
	if key[0] in bigrams_dict_of_dict.keys():
		bigrams_dict_of_dict[key[0]].update({key[1]:count_bigrams[key]}) # used update function to add the value as a dictionary
	else:
		bigrams_dict_of_dict[key[0]]={key[1]:count_bigrams[key]}
for item in bigrams_dict_of_dict.items():
	print(item)

#3 Using tuples
bigrams_dict_of_tuple={}
print()
print("bigrams counts using dictionary of tuples")
print("------------------------------------------------")
for key in count_bigrams.keys():
	if key[0] in bigrams_dict_of_tuple.keys():
		bigrams_dict_of_tuple[key[0]]+=(key[1],count_bigrams[key]) # used + as concationation of two tuples
	else:
		bigrams_dict_of_tuple[key[0]]=(key[1],count_bigrams[key])

for item in bigrams_dict_of_tuple.items():
	print(item)

#Counting trigrams
#=================

#4

list_trigrams = ['can', 'you', 'can', 'a', 'can', 'as', 'a', 'canner', 'can', 'can', 'a', 'can','?']
count_trigrams = {}
for i in range(len(list_trigrams)-2):
	key = tuple(list_trigrams[i:i+3]) # convert result of list slice into tuple
	if key in count_trigrams:
		count_trigrams[key]+=1
	else:
		count_trigrams[key]=1

#Display trigrams counts
print()
print("Trigrams count")
print("==============")

for item in count_trigrams.items():
	print(item)

#5

print()
print("Trigrams to Bigrams counts ratio")
print("================================")

count_bigrams_in_trigrams = {}  # to hold the bigrams count for the trigrams.
count_trigrams_to_bigram_ratio = {} # hold the ratio of trigrams to bigrams count

for i in range(len(list_trigrams)-2):
		key = tuple(list_trigrams[i:i+2])
		if key in count_bigrams_in_trigrams:
			count_bigrams_in_trigrams[key]+=1
		else:
			count_bigrams_in_trigrams[key]=1



for i in range(len(list_trigrams)-2):
	key = tuple(list_trigrams[i:i+3]) # convert result of list slice into tuple
	# trigrams counts divided by bigrams counts
	count_trigrams_to_bigram_ratio[key] =count_trigrams[key]/count_bigrams_in_trigrams[tuple(list_trigrams[i:i+2])] 
	

#Display trigrams trigrams to bigrams counts ratio
for item in count_trigrams_to_bigram_ratio.items():
	print(item)







