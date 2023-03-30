class User:
    """A class to describe users"""

    def __init__(self, first_name, last_name, username, email):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email

    def describe_user(self):
        print(
            f"First Name: {self.first_name.title()}\nLast Name: {self.last_name.title()}\nUsername: {self.username}\nEmail: {self.email}\n")

    def greet_user(self):
        print(f"Greetings, {self.first_name.title()}!")


user_0 = User('zerofirst', 'zerolast', 'zeroeth', 'zero@example.org')
user_1 = User('onefirst', 'onelast', 'oneeth', 'one@example.org')
user_2 = User('twofirst', 'twolast', 'twoeth', 'two@example.org')
user_3 = User('threefirst', 'threelast', 'threeeth', 'three@example.org')

user_0.describe_user()
user_0.greet_user()
user_1.describe_user()
user_1.greet_user()
user_2.describe_user()
user_2.greet_user()
user_3.describe_user()
user_3.greet_user()
