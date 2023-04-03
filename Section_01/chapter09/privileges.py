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


class Admin(User):
    """The Admin class"""

    def __init__(self, first_name, last_name, username, email, privileges):
        super().__init__(first_name, last_name, username, email)
        self.privileges = Privileges(privileges)


class Privileges:
    """a class to describe privileges"""

    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print(f"User has the following privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


admin = Admin('admin', 'admin', 'admin', 'admin@example.org',
              ['can add post', 'can delete post', 'can ban user'])

admin.privileges.show_privileges()
