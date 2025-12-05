
def greet():
    print("Hello! Welcome to Python.")

greet()


def add(a, b):
    return a + b

print("5 + 7 =", add(5, 7))

# Function with default value
def power(num, exp=2):
    return num ** exp

print("Power(5):", power(5))
print("Power(5, 3):", power(5, 3))

# Function returning multiple values
def calculate(a, b):
    sum_val = a + b
    diff_val = a - b
    return sum_val, diff_val

s, d = calculate(10, 4)
print("Sum:", s, "Difference:", d)

# Function with loop inside
def print_table(n):
    print(f"\nMultiplication Table for {n}")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

print_table(7)

# Recursive function
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print("\nFactorial of 5:", factorial(5))
