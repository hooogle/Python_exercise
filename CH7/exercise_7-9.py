sandwich_orders = ['aaa', 'pastrami', 'bbb', 'pastrami', 'ccc', 'ddd', 'pastrami']
finished_sandwiches = []
if 'pastrami' in sandwich_orders:
    print('pastrami sandwich has been selled out.')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    order = sandwich_orders.pop()
    print("I made your " + order + " sandwiches,")
    finished_sandwiches.append(order)
for order in finished_sandwiches:
    print(order)