# v1.0
def my_data_summary(num_lst):
    """returns the following tuple: (total, count, avg).
    This function is implemented at low level for educational purposes."""
    total = 0
    count = 0
    avg = None

    for num in num_lst:
        total += num
        count += 1

    avg = total/count
    return total,count,avg

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

# calculate total, count and avg of num_lst:
ans = my_data_summary(num_lst)
total, count, avg = ans
print("total: ", total, ", count:", count, ", avg: ", avg)
