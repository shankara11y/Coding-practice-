age = 18
if age >= 18:
    print("You are eligible to vote.")

# if-else example
marks = 72
if marks >= 40:
    print("You passed the exam.")
else:
    print("You failed the exam.")

# if-elif-else
num = 0
if num > 0:
    print("Positive number.")
elif num < 0:
    print("Negative number.")
else:
    print("Number is zero.")


speed = 120
if speed > 80:
    print("Over speed!")
    if speed > 120:
        print("Dangerous driving!")
    else:
        print("Drive slowly next time.")


username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login successful!")
else:
    print("Invalid credentials.")


temperature = 35
rain = False

if temperature > 30 or rain:
    print("Weather warning!")
else:
    print("Weather is normal.")
