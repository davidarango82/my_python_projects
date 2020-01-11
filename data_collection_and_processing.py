
# WEEK 2: Map, Filter, and List Comprehensions

# MAP example 1:
myList = [1, 3, 6, 9]
myList3 = list(map(lambda x: x*3, myList))
#print(myList3)
# MAP example 2:
lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]
greeting_doubled = list(map((lambda x: x*2),lst))
#print(greeting_doubled)

# FILTER example 1:
lst = [1, 2, 3, 4, 5, 6, 7]
odd_num_lst = list(filter((lambda x: x % 2),lst))
#print(odd_num_lst)
# FILTER example 2:
lst = ['David', 'Daniel', 'Andrea', 'Juan']
starting_with_D = list(filter(lambda name: name[0] == 'D',lst))
#print(starting_with_D)

# An even better way to do the accumulator pattern:
# List Comprehensions example 'mapping':
numLst = [1, 2, 3, 4, 5, 6, 7]
squared_lst = [x**2 for x in numLst]
# List Comprehensions example 'filtering':
def keep_evens(numLst):
    even_lst = [num for num in numLst if (num % 2 == 0)]
    return even_lst
# Zipping lists example 1:
numLst2 = [num*3 for num in numLst]
zipped_lst = zip(numLst, numLst2)
sum_lst = []
for x, y in zipped_lst:
    sum_lst.append(x + y)

# Using an API (using the requests module found in PyPi)

import requests

# PROGRAM FOR MAKING REQUESTS TO API`S, WITH CACHING
##########################################
import my_api_project_functions
#import json

finished = 'n'
while finished != 'y':

    APIurl = 'https://api.datamuse.com/words'
    my_word = input("write a word: ")

    # search the permanent cache first:
    with open('myCache.txt', 'r') as f:
        content = f.read()
        # if the cache file is empty, initiate the db:
    if content == '':
        my_api_project_functions.initiate_db()

        # #  make the first request to API:
        # res = my_api_project_functions.RequestWrapper(APIurl, my_word, '5')
        # word_lst = res.json()  # extract the json data in the response and return a Python object
        # word_dic = {my_word: word_lst}
        # # create de main database list:
        # main_lst = []
        # # Append the word dictionary to the main list:
        # main_lst.append(word_dic)
        # with open('myCache.txt', 'w') as f:
        #     str_data = str(main_lst)  # parse to string to write to file
        #     f.write(str_data)




