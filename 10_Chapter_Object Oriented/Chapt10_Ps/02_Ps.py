class Calculator:
    def square(self, n):
        return n * n

    def cube(self, n):
        return n * n * n

    def square_root(self, n):
        return n ** 0.5

# Example usage
calc = Calculator()
print(calc.square(4))
print(calc.cube(3))
print(calc.square_root(16))
