sandwich_orders = ['aaa', 'bbb', 'ccc', 'ddd']
finished_sandwiches = []
while sandwich_orders:
    order = sandwich_orders.pop()
    print("I made your " + order + " sandwiches,")
    finished_sandwiches.append(order)
for order in finished_sandwiches:
    print(order)