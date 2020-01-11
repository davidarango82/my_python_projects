
# factorial calculation with recursion
def fac(n):
    if n == 0:
        return 1
    return n * fac(n-1)

def fib(n):
    if n == 0 or 1:
        return 1
    return fib(n-1)+fib(n-2)


result = fib(5)
print(result)
    #0 1 1 2 3 5 8 13 21 34
    #f(0)=0
    #f(1)=1
    #f(2)=f(0)+f(1)
    #f(3)=f(2)+f(1)