#Weight converter 
your_weight = input("Enter your weight: ")
specific_form_weight = input("(L)bs or (K)g: ")

weight_kg = 0.454 * int(your_weight)
weight_l = int(your_weight) / 0.454 

if specific_form_weight.upper() == "L":
    print(f"{weight_kg} kilos")
elif specific_form_weight.upper() == "K":
    print(f"{weight_l} pounds")
else:
    print("No input")