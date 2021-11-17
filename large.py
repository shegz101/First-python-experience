#program to find the largest number in a list
#assume the list is [1,2,4,5,3,6,4,77,56]

number = [1,3,2,5,8,6,9]
max = number[0]

for i in number:
    if i > max:
        max = i
print(max)
