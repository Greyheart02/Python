#while loops

#ex1:

temp = 0
"""
while temp != -1000:
    temp = eval(input("Enter a temperature(-1000 to quit): "))
    print("In fahrenheit i.e ", 9/5 * temp + 32)
"""

#ex2
while temp != -1000:
    temp = eval(input("Enter a temperature(-1000 to quit): "))
if temp != -1000:
    print("In fahrenheit i.e ", 9/5 * temp + 32)
else:
    print("In fahrenheit i.e", 9/5 * temp + 32, ", bye")
