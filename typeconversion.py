birth_year = input("Birth year: ")
print(type(birth_year))
age = 2020 - int(birth_year)
print(type(age))
print(age)

#int() for converting a string into an integer
#float() for converting an string into a float
#bool() for converting a string into a boolean

#Exercise
#Ask a user their weight(in pounds),convert it to kilograms and print on the terminal
your_weight = input("Enter your weight pounds: ")
#1 pound equals 0.454kg
weight_kg = 0.454 * int(your_weight)
print(weight_kg)
