

# command = ""
car_start = False

while True:
    # user input with lower case
    # assigning "help" with variables
    # printing message if input equal to value

    command = input(">").lower()
    if command == "help":
        print("""
    help - for help 
    start - car started
    stop - cat stop
    quit - for quit
        """)

    # assigning values into variables
    # check condition of car start or stop
    # print the condition

    elif command == "start":
        if car_start:
            print("car already started")
        else:
            car_start = True
            print("car started")

    elif command == "stop":
        if not car_start:
            print("car already stopped")
        else:
            car_start = False
            print("car stopped")

    # break the loop

    elif command == "quit":
        print("quit")
        break

    # print the other condition if above conditions are met

    else:
        print("not understand")


















