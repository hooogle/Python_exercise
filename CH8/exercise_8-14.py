def make_car(manufacture, car_type, **other_info):
    car = {}
    car['manufacture'] = manufacture
    car['car_type'] = car_type
    for key, value in other_info.items():
        car[key] = value
    return car

car = make_car('subaru', 'outback', color = 'blue', tow_package = True)
print(car)