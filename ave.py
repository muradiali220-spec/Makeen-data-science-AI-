salary=0
total=0
count=0

while salary>=0:
      salary= float(input("enter the salary or -1 to finish:"))
      total=total + salary
      count=count+1
ave=(total/count)
print("average",ave)
