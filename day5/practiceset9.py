#  create a class "programemr"  for storing information of few programmer working at microsoft . 
class programmer :
    company = "microsoft"

    def __init__(self,name,language,salary):
         self.name = name
         self.language = language
         self.salary = salary

p1 = programmer("vikash","C",12999)
p2 = programmer("nitin","java",2131232)

print(p1.name)
print(p1.language)
print(p1.company)
print(p1.salary)

print()
 
print(p2.name)
print(p2.language)
print(p2.company)
print(p2.salary)





        ## write a class "calculator " capable of finding square ,cube and square root of a numebr 
class Calculator:
        def __init__(self, number):
            self.number = number
        def square(self):
            return self.number ** 2

        def cube(self):
            return self.number ** 3
        def square_root(self):
            return self.number ** 0.5
n = int(input("entre the number :"))
c = Calculator(n)

print("Square =", c.square())
print("Cube =", c.cube())
print("Square Root =", c.square_root())





    # Add a static method in problem 2 to greet the user" hello "
class Calculator:

    @staticmethod
    def greet():
        print("Hello")

    def __init__(self, number):
        self.number = number

    def square(self):
        return self.number ** 2

    def cube(self):
        return self.number ** 3

    def square_root(self):
        return self.number ** 0.5


n = int(input("Enter the number: "))

c = Calculator(n)

Calculator.greet()

print("Square =", c.square())
print("Cube =", c.cube())
print("Square Root =", c.square_root())