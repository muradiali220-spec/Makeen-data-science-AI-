from datetime import datetime
time1= input("enter time1 :")
time2= input("enter time2 :")

time11= datetime.strptime(time1, "%H:%M")
time22= datetime.strptime(time2, "%H:%M")
    
if time1<time2:
         print("time1 comes first ",time1)
     
elif time2<time1:
         print("time2 come before time1",time2)
         
else:
       print("time1 same time2")
       
       
       
       