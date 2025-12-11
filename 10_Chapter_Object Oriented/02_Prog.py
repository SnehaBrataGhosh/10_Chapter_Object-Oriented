#Using self parameter (instance method) and Using @staticmethod

# class Employee:
#     def set_details(self, name, salary, language):
#        name = name
#        salary = salary
#        language = language
#     @staticmethod
#     def company_info():
#         print("This is the Employee class for XYZ Company.")

# # Example usage
# Employee.company_info()  # Call without creating object

# # Example usage
# Jeet = Employee()
# Jeet.set_details("Jee Ghosh", 50000, "Python")
# print(Jeet.name, Jeet.salary, Jeet.language)
# Jeet.company_info()


##################333333333333333333333333333333333333333333333333333333333333333333333333333333333333333

class Employee:
    n = "Jeet"
    salary = 10000
    language = "Py"    
        
    def set_details(self):
        print(f"The name is {self.n} , The sal is {self.salary} , The lang is {self.language}")

Jeet=Employee()
Jeet.set_details()

