while True:
    age = int(input("Please input your age(input 0 to quit):"))
    if age == 0: 
        break
    elif age < 3:
        print("Your ticket is free.")
    elif age < 12:
        print("Your ticket price is 10 dollars.")
    else:
        print("Your ticket price is 15 dollars.")