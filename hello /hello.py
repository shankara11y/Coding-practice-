print("Hello, world!")
print("i am learning python ")
name = "shankar"
age = 18 
height = 44
print(name)
print(age)
print(height)
print(type(name))
print(type(age))
print(type(height))
print("My name is " , name , "and i am " , age , " years old ")
print(f"My name is {name} and i am {age} years old")
your_name = input("Enter your name: ")
print(f"Hello {your_name} , welcome to python ")
a = 10
b = 3
print(a + b) 
print(a-b)
print(a / b)
print(a//b)
print(a%b)
print(a ** b)
x= 10 
y= 20
print(x>y)
print(x==y)
print(y!=x)
print( x>5 and y<25)
print(x>15 or y<25) 
print(not(x>5))

ass= input("Enter your assignment:")
if len(ass) >= 30:
    print("Ass can be submitted ")
else:
    print("Ass cannot be submitted ") 


user= input("Enter your name :")
import random

otp = random.randint(1000, 9999)
print("Your OTP is:", otp)
user=int(input("enter your otp:"))
print("Available rooms: 101, 102, 103, 104, 105, 106")
room = int(input("Choose your room number: "))
if room in [101, 102, 103, 104, 105, 106]:
    print("Welcome", name,)
    print("Your room number", room, "is booked successfully.")
else:
    print("Invalid room number. Please choose from given options.")

