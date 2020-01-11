import numpy as np

arr = np.array([1,2,3])
arr1 = arr.view()  #arr = arr1 --> vars point to the same address
print(id(arr))
print(id(arr1))

m = np.matrix(arr)
print(m)