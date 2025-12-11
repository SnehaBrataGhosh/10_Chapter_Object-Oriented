class Programmer:
    company = "Microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product

# Example usage
p1 = Programmer("Alice", "VS Code")
p2 = Programmer("Bob", "Azure")
print(p1.name, p1.product, p1.company)
print(p2.name, p2.product, p2.company)
