lst = [1,2,3,4,5]

def is_even(n):
    return n%2 == 0

def myfun(a):
    a = a + 1
    return a

lst2 = list(filter(is_even,lst))
print(lst2)

# same implementation using lambda instead of function
lst3 = list(filter(lambda n : n%2 == 0,lst))
print(lst3)

# reduce function
