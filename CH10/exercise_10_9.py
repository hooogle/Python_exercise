filenames = ['cats.txt','dogs.txt']
for filename in filenames:
    try:
        with open(filename) as file_object:
            names = file_object.read()
    except FileNotFoundError:
        pass
    else:
        print(names)