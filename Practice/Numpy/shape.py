import numpy as np

arr_2d=np.array([[1,2,3],[4,5,6.2],[7,8,9],[0,1,0]])
print(arr_2d)
# print(arr_2d.shape)
# print(arr_2d.size)
# print(arr_2d.ndim)
# print(arr_2d.dtype)
# print(arr_2d.itemsize)
# print(arr_2d.nbytes)
# print(arr_2d[2,1])
# arr_2d[2,1]=15
# print(arr_2d)
# print(arr_2d.astype(np.int32))
# arr_2d=arr_2d.astype(np.int32)
# print(arr_2d.dtype)

# s=np.reshape(arr_2d, (6,2))       # Reshape the array to 6 rows and 2 columns
# print(s)

# print(arr_2d[::-1])
# print(arr_2d[:, ::-1])
# print(arr_2d.T)
# print(np.transpose(arr_2d))
# print(np.swapaxes(arr_2d, 0,1))

n=np.insert(arr_2d,1,45,axis=0)
print(n)

m=np.split(arr_2d,2)
print(m)