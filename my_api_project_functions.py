import requests
import json

# This function returns a RESPONSE OBJECT. Caution: needs error handling!
def RequestWrapper(APIurl, word='', max_responses='0'):
    test = int(max_responses)
    payload = {'rel_rhy': word, 'max': max_responses}
    try:
        x = 1/test  # just to generate a TypeError...
        response = requests.get(APIurl, payload)
        return response
    except TypeError:
        print('you need a max value!')

# CODE FOR TESTS:
#data = RequestWrapper('https://api.datamuse.com/words','wine','5')
#print('{} :\n {}'.format(type(data), data))


def initiate_db():
    #  make the first request to API:
    res = RequestWrapper(APIurl, my_word, '5')
    word_lst = res.json()  # extract the json data in the response and return a Python object
    word_dic = {my_word: word_lst}
    # create de main database list:
    main_lst = []
    # Append the word dictionary to the main list:
    main_lst.append(word_dic)
    with open('myCache.txt', 'w') as f:
        str_data = str(main_lst)  # parse to string to write to file
        f.write(str_data)
    print("db initiated.")