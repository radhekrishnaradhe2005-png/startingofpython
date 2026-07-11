## printing table of a random number
num = int(input("entre the number : "))
for i in range(0,11):
     print(f"{num} x {i} = {num * i}")


## write a program to greet all the person in the list ,whose name start with S
l = ["vikash" , "shivam" , "shiv" , "prajesh" , " prachi"]
for name in l:
    if name.startswith("s"):
        print("hwllo",name)


## problem 1 using while loop
num = int(input("entre the number : "))
i =0
while(i<11):
    print(f"{num} x {i} = {num * i}")
    i+=1



    ## write a progra, wheather a given numebr is prime or not
    num = int(input("entre the number "))
    is_prime = True
    for i in range(2,num):
        if(num % i ==0):
            is_prime =False
            break
        if is_prime and num >1:
            print("the prime ")

        else:
            print("not prime")



    
## find the sum of first n natural numbers using while loop
i=1
total =0
while(i<=5):
    total = total+i
    i+=1  
print(total)
   



'''
   *
  ***
 ***** '''
n = int(input("entre the number"))
for i in range(1,n+1):
    print(" " *( n-i) + "*" * (2*i-1))


'''*
       **
       ***
       ****'''
n =int(input("entre the number"))
for i in range(1,n+1):
    print("*"*i)