       #SELECTION STRUCTURE
#is_hot = True

#if is_hot:
   # print("It's a hot day")
#print("Enjoy your day")

is_hot = False
is_cold = True

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:    
    print("It's a cold day")
    print("Wear warm clothes") 
else: 
    print("It's a lovely day")  

print("Enjoy your day")

#Exercise:Price of a house is $1M.
        #if buyer has good credit,
          #they need to put down 10%
    #otherwise
        #they need to put down 20%
    #Print the down payment

is_price = input("Price of house: ")
is_credit_good = True
is_credit_false = False
ten_percent = 0.1 * int(is_price)
twenty_percent = 0.2 * int(is_price)
Price = int(is_price)


if is_credit_good:
    print(ten_percent)
elif is_credit_false:
     print()
else:
    print(Price)

price_house = 1000000

has_credit_good = True

if has_credit_good:
    down_payment = 0.1 * price_house
else:
    down_payment = 0.2 *price_house
print(f"Down payment:  ${down_payment}")    
