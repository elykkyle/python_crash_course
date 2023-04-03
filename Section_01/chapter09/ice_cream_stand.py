class Restaurant:
    """A simple class to describe a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} serves {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is now open.")


class IceCreamStand(Restaurant):
    """A class to describe an ice cream stand"""

    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        print("List of flavors:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")


ice_cream_stand = IceCreamStand('MilkyWay', 'ice cream', [
                                'vanilla', 'chocolate', 'cookies & cream', 'mint chocolate chip'])

ice_cream_stand.display_flavors()
