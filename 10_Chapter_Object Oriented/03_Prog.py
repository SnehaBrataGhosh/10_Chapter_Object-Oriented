# Using __init__()

class Employee:
    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language

# Example usage
Jeet = Employee("Jeet", 50000, "Python")
print(Jeet.name, Jeet.salary, Jeet.language)
