temperature = 30

if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

#Exercise:If name is less than 3 characters long
              #name must be at least 3 characters
          #otherwise if it's more tyhan 50 characters long
             #name can be a maximum of 50 characters
          #otherwise
            #name looks good!

#Solution 
name = "Segun"

if len(name) < 3:
    print("Must be at least 3 characters")
elif len(name) > 50:
    print("Name can be a maximum of 50 characters")
else:
    print("name looks good")
