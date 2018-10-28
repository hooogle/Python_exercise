while True:
    name = input("Please enter your name: ") 
    print("Welcome, " + name + '!')
    with open('guest_book.txt', 'a') as file_object:
        file_object.write(name + ' has come here.\n' )