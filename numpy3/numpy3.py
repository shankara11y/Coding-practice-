import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr)




print(arr[0])



print(arr[1:5])

print(arr.dtype)
print(type(arr))


array = np.array(['apple', 'banana', 'cherry'])
print(array.dtype)
print(type(array))



array1 = np.array([1, 2, 3, 4], dtype='i8')
print(array1)
print(array1.dtype)


arr2 = np.array(['aaa' ,'stud', 3], dtype='a')
print(arr2.dtype)
print((type(arr2)))


arr3 = np.array([1.1, 0, 3.1])
newarr = arr3.astype(bool)

print(newarr)
print(newarr.dtype)

arr4 = np.array([1, 2, 3,4, 5])
x = arr4.view()
arr4[0] = 42
print(arr4)
print(x)


arr5 = np.array([1,2,3,4,5,6,7,8, 9, 10,11,12])
newarr3 = arr5.reshape(4,3)
newarr2 = arr5.reshape(6,2)
print(newarr2)
print(newarr3)




a = np.arange(0,9).reshape(3,3)
print(a[1,:])
def f(x, y=5, *args):
    return x + y + sum(args)
print(f(2, 3, 4, 5))

s = {}
print(s)



arr = np.array([10, 20, 30, 40, 50, 60])

print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))
print("Variance:", np.var(arr))
print("Sum:", np.sum(arr))
print("Minimum:", np.min(arr))
print("Maximum:", np.max(arr))



A = np.array([[1, 2, 3],
              [4, 5, 6]])

B = np.array([[7, 8, 9],
              [10, 11, 12]])

print("Add:\n", A + B)
print("Subtract:\n", A - B)
print("Multiply:\n", A * B)
print("Divide:\n", A / B)