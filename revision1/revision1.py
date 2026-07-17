'''                                                     REVISION                                       '''              

# # Check whether a string is a palindrome.
# n = input(" entre the string: ")
# if n == n[::-1]:
#     print("string is palindrome ")

# else:
#         print(" not")


#  # Remove duplicates from a list.
# l = [1,2,34,3,2,4,2,1]
# res =[]
# for i in l :
#     if i not in res:
#         res.append(i)
#     print(res)
        


# # Check if a number is a prime number.
# n =int(input(" entre the number"))
# isprime=True
# for i in range (2,n):
#     if(n%i==0):
#         isprime=False
#         break

# if(isprime):
#     print("number is prime",n)
# else:
#         print("not prime",n)


   

# Generate the Fibonacci sequence up to n terms.
# n = int(input("entre the number:"))
# a =0
# b=1
# l=[]
# for i in range(n):
#     l.append(a)
#     c = a+b
#     a =b 
#     b =c 

# print(l)


# # Count the number of vowels in a given string.
# string ="umbrella"
# Count=0
# vowels= "aeiou"
# for i in string:
#     if i in vowels:
#      Count+=1

# print(Count)




# # Reverse a string without using built-in reverse functions.
# string = "vikash"
# print(string[::-1])



# while True:
#     num1 = int(input("Enter num 1: "))
#     num2 = int(input("Enter num 2: "))
#     num3 = int(input("Enter num 3: "))

#     if num1 > num2 and num1 > num3:
#         print(f"The greater is {num1}")

#     elif num2 > num1 and num2 > num3:
#         print(f"The greater is {num2}")

#     else:
#         print(f"The greater is {num3}")

#     choice = input("Do you want to continue? (yes/no): ")

#     if choice == "no":
#         break

# print("Finished program...")



#  # Write a program to check whether a number is even or odd.
# n = int(input("entre the number"))

# def evenodd(n):

  
#  for i in range(n+1):
#     if(i%2==0):
#         print("the number is even",i)
#     else:
#         print("odd",i)
# evenodd(n)





# # Remove duplicates from a list.
# l = [1,2,3,1,4,51,1]
# myset = set(l)
# print(myset)
