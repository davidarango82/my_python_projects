# This program includes a function that calculates an employee´s pay 

r = input("input rate: ")
h = input("input hours: ")

def computepay(rate,hours):
    print("computepay function start.")
    rate = float(rate)
    hours = float(hours)
    pay = rate*hours
    return pay

pay = computepay(r,h)
print("The pay of the employee is", pay)
	
