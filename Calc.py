from abc import ABC, abstractmethod


class Operation(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass


class AddOperation(Operation):
    def execute(self, a, b):
        return a + b


class SubOperation(Operation):
    def execute(self, a, b):
        return a - b


class MulOperation(Operation):
    def execute(self, a, b):
        return a * b


class DivOperation(Operation):
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


class Calculator:
    def __init__(self):
        self.operations = {
            "add": AddOperation(),
            "sub": SubOperation(),
            "mul": MulOperation(),
            "div": DivOperation(),
        }

    def add(self, a, b):
        return self.operations["add"].execute(a, b)

    def sub(self, a, b):
        return self.operations["sub"].execute(a, b)

    def mul(self, a, b):
        return self.operations["mul"].execute(a, b)

    def div(self, a, b):
        return self.operations["div"].execute(a, b)
