# This program includes a function that calculates an employee´s pay.
# This version includes time-and-a-half for overtime.

r = input("input rate: ")
h = input("input hours: ")

def computepay(rate,hours):
    print("computepay function start.")
    rate = float(rate)
    hours = float(hours)
    extrahours = 0

    if(hours > 40):
        extrahours = hours - 40
        hours = 40

    pay = rate*hours + 1.5*rate*extrahours
    return pay

pay = computepay(r,h)
print("The pay of the employee is", pay)
	
