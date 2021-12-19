
while True:
    data = input("Enter a number: ")
    if data == "done":
        break
    try:
        num = float(data)
        # compute running total, count and avg:
    except ValueError:
        print("not a number, try again!")

# print total, count and avg: