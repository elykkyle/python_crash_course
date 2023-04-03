class Restaurant:
    """A simple class to describe a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} serves {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is now open.")

    def set_number_served(self, number_served):
        """Sets number served"""
        if number_served < self.number_served:
            print("Cannot set number served to a lower number.")
        else:
            self.number_served = number_served

    def increment_number_served(self, served):
        """Increments number_served by a given amount"""
        self.number_served += served


restaurant = Restaurant('the block', 'american')

restaurant.describe_restaurant()
restaurant.open_restaurant()

print(f"Number served: {restaurant.number_served}")
restaurant.set_number_served(230)
print(f"Number served: {restaurant.number_served}")
restaurant.increment_number_served(29)
print(f"Number served: {restaurant.number_served}")
