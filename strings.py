course = 'Python for Beginners'
#When it is important to use double quote(when you have apostrophe)
course = "Python's Course for beginners"
print(course)

#long String e.g message sent in email use triple quotes
course = ''' 
 Hi daniel ,
 here is our first email sent to you.
 Thank You,
 The support team

'''

print(course)

#Getting character at a given index in the string
course_two = 'Python for Beginners'
print(course_two[0])

#using negative index to get characters from the end
course_two = 'Python for Beginners'
print(course_two[-2])

#Similar way to get few characters of a string
course_two = 'Python for Beginners'
print(course_two[0:4]) #returns all the characters from index 0 to 4,it won't return the character of index 4
 
#Formatted Strings
first = 'John'
last = 'Smith'
message = first + ' [ ' + last + ' ] is a coder'
msg = f'{first} [{last}] is a coder'
print(message)
print(msg)

#String Methods
course = 'Python for Beginners'
#using a built-in function len to get the lenght of a character
print(len(course))
#Using the replace method
print(course.replace('P','j'))
print(course.replace('Beginners','Absolute Beginners'))

#using "in" method to know if a character/word  is in a string
print('Python' in course)