class ok:
    def __init__(self,n):
          self.n = n

    def __add__(self,num):
            return self.n + num.n

n=ok(1)
m= ok(2)
print(n+m) 



# Constructors (__init__)

# Q4. Employee Class
# Store:

# name
# salary
# department

# Create 3 employee objects and print their details.
class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

e1 = Employee("Vikash", 50000, "CSE")
e2 = Employee("Rahul", 60000, "IT")
e3 = Employee("Nitin", 70000, "HR")

print(e1.name, e1.salary, e1.department)
print(e2.name, e2.salary, e2.department)
print(e3.name, e3.salary, e3.department)