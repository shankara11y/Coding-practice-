# age = 16 
# if age >= 18: 
#    print("you can vote")
# else:
#    print("You cant vote ")

# age = 20 
# has_id = True 
# if age >= 18 and has_id:
#   print("You can enter ")
# else: 
#   print("you cant enter ")


# for i in range(1, 6):
#    print(i)

# for ch in "letter":
#    print(ch)

# for letter in "Shabnam " :
#    print(letter )we

# i = 1 
# while i <= 5:
#     print(i)
#     i = i + 1 

# for i in range(1, 10):
#     if i == 5 :
#         break 
#     print(i)

# for i in range(1, 6):
#     if i == 3 :
#        continue
#     print(i)

# total = 0 
# for i in range(1, 101):
#   total = total + i 
# print("sum=", total )

# for i in range(1, 20 , 2):
#     print(i)

# def greet():
#     print("hello , welcome to python ")
# greet()

# def greet(name):
#     print("hello ," , name)
# greet("sh")


# def add(a, b):
#     return a + b 
# result = add(2, 3)
# print("Sum:", result )

# A function that prints your name.
# def printname():
#     print("My name is Shankar ")
# printname()

#func thats adds two numbers
# def add(a, b):
#     print("Sum :", a+b)

# add(2, 3)

# def mult(a, b, c):
#     return a*b*c
# result = mult(2, 3, 4)
# print("mult:", result)


#function that checks if the no. is even or odd 
# def check(num):
#     if num %2 == 0 :
#         print(f"{num} is even" )
#     else:
#         print(f"{num} is odd ")

# check(6)

# colors = ("red", "green", "blue")

# for c in colors:
#     print(c)

# point = (5, 10, 15)
# x, y, z = point
# print(x, y, z)


# nums = (10, 20, 30, 40, 50)
# print(nums[0])   # first
# print(nums[4])  # last
# nums = (10, 20, 30, 40, 50)
# print(30 in nums)
 
# nums = (1, 2, 3)
# temp = list(nums)
# temp.append(4)
# nums = tuple(temp)
# print(nums)

# fruits = ["apple", "banana", "mango"]

# for f in fruits:
#     print(f)

# print(fruits)


# nums = [10, 20, 30, 40, 50]
# print(nums[1:4])    # [20, 30, 40]
# print(nums[:3])     # [10, 20, 30]
# print(nums[2:])     # [30, 40, 50]



   # 7. Take 5 numbers from user and store in list

# numbers = []

# for i in range(5):
#     num = int(input("Enter a number: "))
#     numbers.append(num)

# print("Your list:", numbers)

#Reverse the list using slicing
# lista = [10, 20, 30, 40, 50]
# print(lista[::-1])


# colors = ("red", "green", "blue")

# for o in colors:
#     print(o)


t = (2, "a", "b", "ayfdg", 3)
print(t)
print(t[0])
print(t[4])
print(t[1:4])

tt = list(t)
tt.append(5)
t = tuple (tt)
print(t)


# Nested tuple access
t = (10, 20, (30, 40, 50))
print(t[2][1])   # Output: 40

name = "shankar"
t = tuple(name)
print(t)        #('s', 'h', 'a', 'n', 'k', 'a', 'r')

#Convert tuple of strings to uppercase.
t = ("apple", "banana", "cat")
t2 = tuple(x.upper() for x in t)
print(t2)

#tuple of coordinates → print distance from origin.
points = ((3, 4), (5, 12), (8, 15))

for x, y in points:
    d = (x**2 + y**2) ** 0.5
    print("Distance:", d)



person = {"name " : "shankar "
          , "age " : 18 , 
          "city " : "thane "}
print(person)
print(person["name "])

person["clg "] = "itm"
print(person)

