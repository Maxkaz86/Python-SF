import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calculator = Calculator

    def test_multiply(self):
        assert self.calculator.multiply(self, 2, 2) == 4

    def test_division(self):
        assert self.calculator.division(self, 10, 2) == 5

    def test_adding(self):
        assert self.calculator.adding(self, 128, 10) == 138

    def test_subtraction(self):
        assert self.calculator.subtraction(self, 10, 4) == 6

    def teardown(self):
        print('Выполнение метода Teardown')