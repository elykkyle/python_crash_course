class Restaurant:
    """A simple class to describe a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} serves {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is now open.")


restaurant_0 = Restaurant('the block', 'american')
restaurant_1 = Restaurant('acapulco', 'mexican')
restaurant_2 = Restaurant('the olive garden', 'italian')

restaurant_0.describe_restaurant()
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
