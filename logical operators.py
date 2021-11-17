has_high_income = False
has_good_credit = True

#Logical And Operator AND:Both conditons should be true

if has_high_income and has_good_credit:
    print("Eligible for loan")

#Logical Or Operator  OR:At least one condition should be true

if has_high_income or has_good_credit:
    print("Eligible for loan")

#Logical Not Operator : It negates the condition
has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")