class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)
    def open_restaurant(self):
        print("The restaurant is opening!")
restaurant1 = Restaurant('canguan1','cuisine1')
restaurant1.describe_restaurant()
restaurant2 = Restaurant('canguan2','cuisine2')
restaurant2.describe_restaurant()
restaurant3 = Restaurant('canguan3','cuisine3')
restaurant3.describe_restaurant()