numbers = [10, 20, 30, 40, 50]
print("Numbers:", numbers)

print("First element:", numbers[0])
print("Last element:", numbers[-1])

numbers.append(60)
numbers.insert(2, 15)
print("\nAfter adding:", numbers)

numbers.remove(30)
popped = numbers.pop()
print("After removing:", numbers)
print("Popped value:", popped)

# Looping through list
print("\nLooping through list:")
for num in numbers:
    print("Number:", num)

# List comprehension
squares = [x * x for x in range(1, 11)]
print("\nSquares from 1 to 10:", squares)

# Sorting
unsorted_list = [5, 3, 8, 1, 9]
unsorted_list.sort()
print("\nSorted list:", unsorted_list)

# 2D list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("\n2D Matrix:")
for row in matrix:
    print(row)

# Searching item
if 40 in numbers:
    print("\n40 found in numbers!")
else:
    print("\n40 not found.")
