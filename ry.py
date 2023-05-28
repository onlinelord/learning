'''     CALCULATOR       '''
'''
name=input("please type ur name:")
a = int(input("first number:"))
b =int(input("second number:"))
c= input("operation")
  
if(c=="+"):
  print("addition of a and b is",a+b)
elif(c=="-"):
  print("sub of a and b is",a-b)
elif(c=="*"):
  print("multiplication of a and b is",a*b)
elif(c=="/"):
  print("division of a and b is",a/b)
elif(c=="%"):
  print("remainder is:",a%b)
else:
  print("operation doesn't exist please perform following operation only {+,-,*,/} ")
print("thanks Mr",name,"for using our service")

'''






'''    TABLE GENERATOR    '''
'''
r=int(input("kiski table chahiye:"))
x=int(input("kitne tak:"))
i=0
while(i<x):
  print(r,"×",i+1,"=",r*(i+1))
  i=i+1
'''



'''factorial calculator'''

'''
def factorial(n):
  if (n==0):
    return 1
  elif (n==1):
    return 1
  else:
    return n * factorial(n-1)
k=int(input("u want factorial of:"))
print("factorial of ",k,"is :")
print(factorial(k))
'''



'''online time getting tool'''
'''
import time 
timevalue=time.strftime('%H:%M:%S')
hour=int(time.strftime('%H'))
mint=int(time.strftime('%M'))
sec=int(time.strftime('%S'))
if (hour > 12):
 print (hour-12,':',mint,':',sec)
else :
 print ("time is",hour,':',mint,':',sec)
 '''
 
 
