#Question 1 – Variables and Input

name:input("enter your name :")
age:int(input("enter your age :"))
print(" Helle ", name + "you are" ,str (age )+ "years old")

#Question 2 – Data Types and Arithmetic Operators

num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
summ=num1+num2
print("the sum is",summ)         

#Question 3 – Arithmetic and Relational Operators
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
x= True
if num1>num2:
 print("is the first number greater?", x)         

#Question 4 – Boolean Operators
 age=int(input("Enter your age:"))
nationality=(input("Enter your nationality:"))
if age>=18 and nationality=="omani":
     print( "eligible to vote in oman ") 
else:
    print( "ineligible to vote in oman ") 
 
#Question 5 – If Statement
num=int(input(" enter a number: "))
if num>=0:
        print(" the number is positive.")
else:
        print(" the number is negative.")

#Question 6 – If / Else
 num=int(input(" enter a number: "))
if num%2==0:
        print(" the number is even.")
else:
        print(" the number is odd.")

#Question 7 – If / Elif / Else
mark=int(input(" enter your marks: "))
if mark>=90:
        print(" Excellent")
elif mark>=70 and mark<90:
        print(" Good")
elif mark>=50 and mark<70:
        print(" Good")
else:
    print("Fail")
    
    
#Question 8 – Nested If        
age=int(input(" how old are you? "))
licensee= input("do you have driving license? yes or no : ")
yes= True
no=False
if age>=18 and licensee== "yes":
        print(" you can drive.")
elif age>=18 and licensee== "no":
        print(" you need a license to drive.")

else:
     print(" you are too young to drive.")
  
#Question 9 – While Loop
counter=0
while counter<5:
      counter=counter+1
      print(counter)
#Question 10 – While Loop with If Condition  
 num=int(input("enter a number: "))
counter=0
while   counter<num:
     if counter%2==0:
        counter=counter+2
     print(counter)
  
           
        