## write a progrma to find the greatest of two numbers using functions 
'''def fun(a,b,c):
    if a > b and a > c:
        print("greater is a",a)
    elif b > a and  b > c:
        print("greater is b",b)
    else:
        print("greater is c",c)
 
      

n=fun(1,2,3)
print(n)'''


##  in python to prevent print() function to go to the new line we use 
'''     end=""     '''
## this can stop print() function to \n



## write a recursive function to calculate the sum of first n natural numbers 
'''n = int(input("entre the number:"))
def sum(n):
 if n == 1:
    return 1

 return n + sum(n-1)

res = sum(n)
print(res) '''

