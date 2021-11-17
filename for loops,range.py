#for loops to iterate through a word
for item in 'Python':
    print(item)

#defining a list using square bracket
for item in ['Mosh', 'segun','sarah']:
    print(item)

#looping over a list a number
for item in [1 , 2 , 3 , 4]:
    print(item)

#using the range function for a range of numbers range()
for item in range(10):
    print(item) # print out the numbers from 0 to 9 with the exclusiomn of the number inputted

for item in range(5, 10):
    print(item)  # print out the numbers from 5 to 9 with the inclusion of the first number and exclusiomn of the last number

#range function with two numbers,indicating the first and last number with a step number to jump through

for item in range(5, 10, 2):
    print(item)


#Exercise
#Write a program to calculate the total cost of all the items in an imaginary shopping cards
#prices = [10 , 20 , 30]

prices = [10,20,30]
total = 0
for price in prices:
    total += price 
print(f"Total: {total}")


x = 50

total = 0

for x in range(1,x+1):
    total += number
print("Sum of 1 until %d: %d" % (x, total))

