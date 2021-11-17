#range function
print(range(5))

#absolute function
print(abs(-10))

#absolute value having complex number as argument returns magnitude of the absolute value
print(abs(3 + 4j))  #result:5.0

#maximum function
print(max(2,3,4,6))  #result:6

#minimum function
print(min(2,3,-1,0,-7)) #result:-7

#type function:returns the data type of the given argument
type("this is a string")

#len():returns the length of an object or the number of items in a list given as argument.
print(len("jhgfdsxcvbnxjgbgsvvhha"))

def your_choice(answer):
    if answer > 5:
        print("you are overaged")
    elif answer <= 5 and answer > 1:
        print("welcome to toddler's club")
    else:
        print("you are too young for toddler's club")

print(your_choice(6))
print(your_choice(4))
print(your_choice(3))

def your_score():
    print("i love pizza")

print(your_score())

#function to run absolute value for python
def abs_value(number):
    if number >= 0:
        return number
    else:
        return -number

print(abs_value(8))
print(abs_value(-3))

#function to run the addition of two digits
def add_value(a,b):
    return a + b
print(add_value(2 , 3))

#function can call other function
def members_total(n):
    return n * 3

def org_total(m):
    return members_total(m) + 5

print(org_total(2))
print(org_total(5))
print(org_total(10))






