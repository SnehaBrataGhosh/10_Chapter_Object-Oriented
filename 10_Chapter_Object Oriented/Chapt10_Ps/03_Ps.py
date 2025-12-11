class MyClass:
    a = 10

obj = MyClass()
obj.a = 0  # Changes only for this object, not the class
print(obj.a)       # 0
print(MyClass.a)   # 10 → class attribute remains unchanged
