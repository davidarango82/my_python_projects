
def f(a, L = []):  # default argument
    L.append(a)
    return L


lst1 = []

'''print(f(1))
print(f(2))
print(f("a"))
print(f("a", lst1))
print(lst1)'''

#print(int("100", 2))

#  LAMBDA FUNCTIONS


def func(x):
    return x+1


#print(func(1))

#print((lambda x,y: x+y)(y=5, x=1))


# Tuples: Sorting and breaking ties

tups = [('bassy', 3, 2 ),
        ('aarrr', 4, 1),
        ('car', 5, 6)]


def func(tup):
    print('func executed')
    return tup[1]


def word_len(tup):
    return len(tup[0])

print(sorted(tups, key = lambda tup: (len(tup), tup[0])))

dict = {"a":[1,2,6], "b":[5,4,9], "c": [7,8,9]}

for key in dict:
    print(dict[key][0])

