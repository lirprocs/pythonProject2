class Calculator:
    def __init__(self):
        self.result = 0
        self.last_operation = None

    def sum(self, a, b):
        result = a + b
        self.last_operation = f'sum({a}, {b}) == {"{:.1f}".format(result) if type(result) == float else result}'
        return result

    @classmethod
    def clear(cls):
        cls.last_operation = None

# Пример использования метода clear
calc = Calculator()
calc.sum(5, 10)
print(calc.last_operation)  # Выведет: add 5

Calculator.clear()
print(calc.last_operation)  # Выведет: None
