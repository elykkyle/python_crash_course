class Employee:
    """Class to describe an employee"""

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, annual_raise=5000):
        self.salary += annual_raise
