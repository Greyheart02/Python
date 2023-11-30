#while loops

#ex1:

temp = 0
"""
while temp != -1000:
    temp = eval(input("Enter a temperature(-1000 to quit): "))
    print("In fahrenheit i.e ", 9/5 * temp + 32)
"""

#ex2
"""
while temp != -1000:
    temp = eval(input("Enter a temperature(-1000 to quit): "))
if temp != -1000:
    print("In fahrenheit i.e ", 9/5 * temp + 32)
else:
    print("In fahrenheit i.e", 9/5 * temp + 32, ", bye")
    """


#ex4
"""
for i in range(10):
    print(i)
"""

#ex4
"""
i = 0
while i < 10:
    print(i)
    i = i + 1
"""
"""
temp = eval(input("Enter a temperature in celcius: "))

if temp < -273.15:
    print("That temperature is not possible.")
else:
        print("In fahrenheit i.e ", 9/5 * temp + 32)
"""
"""
temp = eval(input("Enter a temperature in celcius: "))    
while temp < -273.15:
    temp=eval(input("Impossible. Enter a valid temperature"))
print("In fahrenheit i.e ", 9/5 * temp + 32)
"""
#ex:
"""
i = 0
while i < 50:
    print(i)
    i = i+ 2
    print("bye bye")
"""

#infinite loops
#ex1
"""
i = 0
while i < 10:
    print(i)

    """


while True:
    temp = eval(input(":"))
    if temp == -1000:
        print("bye")
        break
    print(9/5 * temp + 32)




