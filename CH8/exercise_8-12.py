def make_sandwich(*toppings):
    print("Making a sandwich with the following toppings:")
    for topping in toppings:
        print("-" + topping)
make_sandwich('pepperoni')
make_sandwich('pepperoni', 'green peppers')
make_sandwich('aaa', 'bbb', 'vvv')