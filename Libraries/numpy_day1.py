import numpy as np

# num = np.array([1,2,3,4,5])
# num = num*2

# #a0
# a0 = np.array(55)

# #a1
# a1 = np.array([11,22,33,44,55])

# #a2
# a2 = np.array([[11,22,33,44],[66,77,88,99]])

# #a3
# a3 = np.array([[[1,2,3],[4,5,6]],[[4,5,6],[7,8,9]]])

# print(a2.ndim)
# print(a3.dtype)
# print(a3.shape)
# print(a3)
# print(a3.size)

a = np.zeros((3,))
print(a)

ar = np.zeros((3,5))
print(ar)

a1 = np.ones((2,3))
print(a1)

a2 = np.full((2,3),100)
print(a2)

a3 = np.arange(5,11,1)
print(a3)