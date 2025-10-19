c= float(input("enter the temp :"))
f= ((c*9/5)+32)
c1=((f-32)*(5/9))
erroe_rate=0.00005

diff= c1-c
print(diff)
if diff<error_rate:
    print(" execute")
else:
    print("  not execute")
    
if c1==c:
    print("conversion is perfect")
    
else:
     print("conversion is not exact it is",c1)
     
     
     #000000000
       from math import sqrt
 
  x=sqrt
  y= 2.0
  error_rate=0.00005
  diff= x*x-y
  
  if diff<error_rate:
      print(" sqrt2 x sqrt2 equal 2 pleas "