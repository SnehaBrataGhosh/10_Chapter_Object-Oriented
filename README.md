Chapter 10 – Object Oriented Programming (OOP)

Overview
This folder contains beginner OOP examples using classes and objects. The programs cover class attributes vs instance attributes, instance methods with self, constructors (__init__), static methods, and a few small “real world style” class exercises.

Concepts Covered
- Defining classes and creating objects
- Class attributes vs instance attributes
- Instance methods and the self parameter
- Constructors using __init__()
- @staticmethod for utility methods
- Updating object state inside methods
- Understanding that “self” is just a conventional parameter name

Code Highlights
- Basic Employee class showing attributes and setting an instance attribute (name)
- Printing instance details using self inside a method
- Employee class using __init__() to initialize fields
- Programmer class with a shared company attribute and per-instance product/name
- Calculator class with square/cube/square_root methods
- Example showing that changing obj.a does not change the class attribute MyClass.a
- Static method example (Calculator.greet())
- Train class exercise:
  - Track available seats
  - Book tickets by decreasing seats
  - Print status and fare info
- A small example showing that the first method parameter can be named anything (not only “self”)

Learning Outcome
I learned how to structure code using classes, how object state works, and how methods/constructors help keep related logic together. These basics are useful later for larger projects and clean code organization.
