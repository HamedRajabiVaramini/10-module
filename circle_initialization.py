'''
simple_programming_

This code defines circle module with 
one variable (PI) and two functions
and initialization 

These lines are going to be executed when 
this module imported for the first time 
'''  
print("This is circle module")
print("It has PI and two functions")
i = 1
sum = 0
while i <= 100:
    sum += i 
    i+=1

PI = 3.14159

def area(radius):
    return (radius ** 2) * PI

def circumference(radius):
    return 2 * radius * PI

