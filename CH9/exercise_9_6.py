class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)
    def open_restaurant(self):
        print("The restaurant is opening!")
    def set_number_served(self, number_served):
        self.number_served = number_served
    def increment_number_serbed(self, increment_number):
        self.number_served = self.number_served + increment_number


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, *flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
    def describe_ice_cream_stand(self):
        super().describe_restaurant()
        print(self.flavors)

ice_cream_stand1 = IceCreamStand('ice1', 'cuisine1', 'vanila', 'apple', 'strawbary')
ice_cream_stand1.describe_ice_cream_stand()