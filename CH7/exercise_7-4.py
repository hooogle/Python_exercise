message = "Please input an pizza material(input 'quit' to end): "
while True:
    material = input(message)
    if material != "quit":
        print("We will add " + material + "to your pizza.")
    else:
        break