
print("Numbers from 1 to 10:")
for i in range(1, 11):
    print(i, end=" ")
print()


fruits = ["apple", "banana", "mango", "orange"]
print("\nFruit names:")
for fruit in fruits:
    print("I like:", fruit)

print("\nMultiplication Table (1 to 5)")
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end="\t")
    print()



print("\nCounting till 5 using while loop:")
count = 1
while count <= 5:
    print("Count:", count)
    count += 1

print("\nCountdown from 5 to 1:")
num = 5
while num > 0:
    print(num)
    num -= 1

print("\nStop when number hits 7:")
for i in range(1, 11):
    if i == 7:
        print("Hit 7! Breaking loop.")
        break
    print(i)


print("\nSkipping even numbers:")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)


