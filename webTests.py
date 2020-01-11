import random

def char_freq(st):
    d = {}
    for c in st:
        if c not in d:
            d[c] = 0
        d[c] = d[c] + 1
    return d


def best_key(dic):
    key_lst = list(dic.keys())  # list of dict keys to be able to iterate
    best_ky = key_lst[0]  # init key assoc. w/ highest val
    for key in key_lst:
        if dic[key] > dic[best_ky]:
            best_ky = key
    return best_ky


def most_freq_letter(st):
    dic = char_freq(st)
    return best_key(dic)


#print(most_freq_letter('aaabbbcccccddd'))


def my_fun(x, y):
    print(x)
    print(y)


x = ("a", "b")
my_fun(*x)  # unpacking a tuple as function arguments

vs = "david",1,"andrea"
name, wives, name_wife1 = vs

dic = {"a": 1, "b": 4, "c": 7}

for k, v in dic.items():
    print("key: {} value: {}".format(k, v))
d_items = dic.items()
print("d_items: {}".format(d_items))
items_list = list(d_items)
dic.pop('b')
print(dic)
print("d_items: {}".format(d_items))

print(("a", 1) in items_list)

print("bye")
