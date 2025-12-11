class Calculator:
    @staticmethod
    def greet():
        print("Hello!")

    def square(self, n):
        return n * n

# Example usage
Calculator.greet()
calc = Calculator()
print(calc.square(5))
