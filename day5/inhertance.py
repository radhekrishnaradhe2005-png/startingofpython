# class emp:
#     def  employee(self,name):
#         self.name = name
#         print(f"this the employee of the year {self.name} his name ..")

# na = emp()
# na.employee("vikash")




##  multiple inheritance 
class inheritance:
       fun = "have fun"
       def fun(self):
         print(f"this function is called fun .. which means we will ")

class another:
        def child(self):
            print(" this would be empty ")

class calling(inheritance,another):
        def ok(self):
         print(" this can have the property of both the class")
   
a = inheritance()
c= calling()
c.fun()
c.child()
c.ok()
a.fun()