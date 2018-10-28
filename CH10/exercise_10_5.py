filename = 'love_program_reasons'
while True:
    message = input("Why are you so like programming?")
    with open(filename, 'a') as file_object:
        file_object.write(message + '\n')
