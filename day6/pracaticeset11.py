## WRTIE A PROGRAM TO FIND IF THE FILE 1.TXT IS PRESENT IS THERE OR NOT ..
try:
 with open("1.txt","r") as f:
   print(f.read())
   
except Exception as e:
 print(e," yes i do not find any file ")
