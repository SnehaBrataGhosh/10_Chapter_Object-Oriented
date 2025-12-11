class Example:
    def show(harry, name):  # 'self' replaced with 'harry'
        print(f"Hello {name}")

obj = Example()
obj.show("Ranabir")  # Works the same as 'self'
