order=int(input("how many candies?"))
av=4
count=1
while count<=order:
    if count>av:
        print('out of stock')
        break
    print("candy")
    count+=1
for i in range(0,5):
    print(i)
print('bye')