"""
lis=[]
while True:
    inputstr=input("enter an element or qtoo exit/stop:")
    if inputstr.isdigit():
          lis.append(int(inputstr))
    elif inputstr[0]=='-' and inputstr[1:].isdigit():
          lis.append(int(inputstr[1:])*-1)     
    elif inputstr=="q":
       break
    else:
        lis.append(inputstr)
print(lis)
"""                         



"""

positive=[]
negative=[]
while True:
number=input("print number or q to stop:")
     if number=="q":
         break
     else:
         number=input(int("integer"))
        if number>=0:
          positive.append(number)
        else:
            negative.append(number)
print(positive, negative)         
   """      



#Q:Question 1: Collect Positive and Negative Numbers
"""
Ask the user to enter integers (positive or negative) until they type "q".
Store positive numbers in one list and negative numbers in another.
Then print both lists.
positive=[]
negative=[]
while True:
number=input("print number or q to stop:")
     if number=="q":
         break
     if number.isdigit():
        number=int(number)
        positive.append(number)
     else:
            number[0]=="-":
            number=int(number[1:])*-1  
            negative.append(number)
print(positive, negative)         
 """
Question 2: Sum of Numbers

Keep asking the user to enter numbers until "done" is typed.
Ignore any non-numeric input.
At the end, print the sum of all valid numbers entered.

numbers=[]
while True:
    num=input("enter number or done:")
    if num=="done":
     break
    elif num.isdigit():
      numbers.append(int(num))
      
    elif num[0]=="-":
      num=int(num[1:])*-1 
      numbers.append(num)
     
print(sum(numbers))    
