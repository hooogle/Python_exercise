from exercise_9_6 import Restaurant

restaurant = Restaurant('res1','cuisine1')
print(restaurant.number_served)
restaurant.number_served = 10
print(restaurant.number_served)
restaurant.increment_number_serbed(10)
print(restaurant.number_served)