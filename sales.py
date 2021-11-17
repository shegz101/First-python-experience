#Program to compute the sales tax and tips on a restaurant meal
#Meal cost = $50.00
#sales tax rate = 6.6%
#tip = 20% of meal + tax

meal = 65.00
tax = 6.6/100
tip = 20/100 * meal + tax

meal = meal + meal*tax

total = meal + meal*tip

print(meal)
print(total)


name = input("may i know me? ")
print("It’s a pleasure to meet you" + name + "!")
age = input("Your age, please? ")
print("So, you’re " + age + "years old," + name + "!")



