# a simple function example
def add_sub(x,y):
    a=x+y
    b=x-y
    return a,b

res1,res2 = add_sub(5,4)

# Function arguments: position, keyword, default and variable length

# keyword arg example:
def myfun(age,sex):
    print("Age:",age)
    print("Sex:",sex)
myfun(sex="M",age=10)

# default arg example:

def myfun2(sex,age=15):
    print("Age:",age)
    print("Sex:",sex)
myfun2("F")

# variable length arg example: ("*" represents a tuple)
def myfun3(*a):
    print(type(a))
    b=0
    for i in a:
        b+=i
    print(b)
myfun3(1,2,3)

# keyworded variable length arg example:
def person(name,**a):
    print(name)
    print(a)
person("David",age=37,sex="M") #returns a dictionary

