import math



n = int(input("enter the number of partitions "))
a1 = input("enter the beginning of the segment   ")
b = float(input("enter the end of the segment   "))
print("\nroot: math.sqrt() \nModule: abs() \nexponentiation: **")
function = input("\nenter a function with the variable 'x'   ")

a = float(a1)
prev = a
temp = a
d = b - a
SmallCount = d/n                                                ## length of a single partition
s1 = float(0)
s = float(0)


while prev <= b:
    prev = str(temp)
    Function_RN = ''.join(function).replace('x', prev)
    Function_Count = eval(Function_RN)                          ## function value at the moment
    prev = float(prev)
    s1 = ((temp + SmallCount) - prev) * Function_Count          ## area of one rectangle
    s += s1                                                     ## total area
    temp += SmallCount
    prev = temp

print("Area =   ", s)

input("press enter to exit")
