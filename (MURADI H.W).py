#Problem 1: Hello, Variables! 
name= ("ali")
age= (25)
height= (1.68)
print("Hello, my name is " ,name + " I am " ,str(age) + " years old and my height is", str(height) + " meters.")

#Problem 2: Basic Arithmetic
num1=int(input("Enter first number: "))
num2=int(input("Enter second number:"))
add= num1+ num2
print(add)
subb= num2-num1
print(subb)
mull= num1*num2
print(mull)
divv=num1/num2
print(divv)

#Problem 3: Data Type Check
a= 20
b= 45.6
c= "muradi"
print(type(a))
print(type(b))
print(type(c))


#Problem 4: Area of a Rectangle
length=int(input("length: "))
width=int(input("width: "))
area=length * width
print(area)

#Problem 5: Simple Interest Calculation
P= float(input(" principal amount :"))
R= float(input("rate of interest : "))
T= float(input(" time in years : "))
interest =(P * R * T)/(100)
print(interest)
