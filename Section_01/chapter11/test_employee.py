import pytest
from employee import Employee


@pytest.fixture
def employee():
    employee = Employee('jane', 'doe', 50000)
    return employee


def test_give_default_raise(employee):
    employee.give_raise()
    assert employee.salary == 55000


def test_give_custom_raise(employee):
    employee.give_raise(10000)
    assert employee.salary == 60000
