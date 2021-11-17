#car Game

controls = "" 
started = False
while True:
    controls = input("> ").lower()
    if controls == "start":
        if started:
            print("car is already started!")
        else:
             started = True
             print("Car stared....")
    elif controls == "help":
                print("""
 start - to start the car
 stop - to stop the car
 quit - to exit       
        """)
    elif controls == "stop":
        if not started:
            print("car is already stopped")
        else:
            started = False
            print("car has stopped...")
    elif controls == "quit":
        break
    else:
        print("I don't understand this control....")




