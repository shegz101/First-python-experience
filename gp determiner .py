#The python gp input 

grade_point = int( input("Put In Score ") ) 

if grade_point >= 70:
    print("Wow,you have an A")
elif grade_point < 70 and grade_point > 59:
    print("YOu have a B,try better next time to get an A")
elif grade_point < 60 and grade_point > 49:
    print("You have a C,this is a fair score")
elif grade_point < 50 and grade_point > 45:
    print("This is a low score,you have a D ,try better nwxt time")
elif grade_point < 46 and grade_point > 39:
    print("THis is really a very very low score , you have a E")
else:
    print("You have an F,you got a carryover in this course based on your poor performance")



