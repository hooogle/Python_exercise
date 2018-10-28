import json


filename = 'favorite_numbers.json'


try:
    with open(filename) as f_obj:
        number_temp = json.load(f_obj)
except FileNotFoundError:
    number = input("Please input you favorite number: ")
    with open(filename, 'w') as f_obj:
        json.dump(number, f_obj)
else:
    print("I know your favorite number! It's " + number_temp + '.')