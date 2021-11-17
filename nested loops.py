#we can use nested loops to print out things like coordinate
for x in range(4):
    for y in range(3):
        print(f'({x} , {y})')

#Challenge use nested loops to draw capital letter F
#Hint: numbers = [5,2,5,2,2] gives number of X on each line
 
numbers = [5,2,5,2,2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'X'
    print(output) #prints out F

print("i am a hero")

#to print L
digits = [2,2,2,2,5]
for l_count in digits:
    result = ''
    for numbering in range(l_count):
        result += 'X'
    print(result) #prints L
