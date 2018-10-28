favoriate_places = {
    'Alice': ['Beijing', 'Nanjing', 'Shanghai'],
    'Bob': ['Tokyo'],
    'Tom': ['Guangzhou', 'HongKong'],
    }
for name, place in favoriate_places.items():
    if len(place) == 1:
        print(name + '\'s favoriate place is:')
        print(place)
    else:
        print(name + '\'s favoriate places are: ')
        print(place)
