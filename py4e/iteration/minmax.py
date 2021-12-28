# v1.0
# This program needs further thought: The function itself will return with non-numeral params.
# Protection from the program that uses the function is needed, but is this appropriate?
def min_max(lst):
    """ Assumes param lst is a list of numbers.
        Returns a tuple (min, max)."""
    my_min = None
    my_max = None
    for num in lst:
        if (my_min and my_max) is not None:
            # recalculate running min and max:
            if num < my_min:
                my_min = num
                continue
            if num > my_max:
                my_max = num
        else:
            my_min = num
            my_max = num
    ans = (my_min, my_max)
    return ans


num_lst = []
while True:
    data = input("Enter a number: ")
    if data == "done":
        break
    try:
        num = float(data)
        # add number to num_lst:
        num_lst.append(num)
    except ValueError:
        print("not a number, try again!")

# find the min and max of the list:
ans = min_max(num_lst)
print(ans)
