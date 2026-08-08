import numpy as np

# Task 1: Create Arrays

array = np.array([10,20,30,40,50])
print(array)
a1 = np.zeros((10))
print(a1)

a2 = np.ones(10)
print(a2)

a3 = np.arange(1,21)
print(a3)

a4 = np.arange(2,21,2)
print(a4)

# Task 2: Array Attributes

array = np.array([[1,2,3],[4,5,6],[1,4,8]])
print(array.shape)
print(array.size)
print(array.ndim)
print(array.dtype)
print(array.itemsize)

# Task 3: Reshape

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(arr)
print(arr.reshape(3,4))
print(arr.reshape(4,3))
print(arr.reshape(2,6))
print(arr.reshape(6,2))

# Task 4: Flatten

arr1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr1)
ar = arr1.flatten()
print(ar)
arr = arr1.ravel()
print(arr)

# Task 5: Transpose
print(arr1.T)

# Task 6

a = np.array([1,2,3])
b = np.array([4,5,6])
c = np.concatenate((a,b))
print(c)

ha = np.hstack((a,b))
print(ha)

va = np.vstack((a,b))
print(va)

da = np.dstack((a,b))
print(da)

# Task 7

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)

b = np.array([[11,22,33],[44,55,66],[77,88,99]])
print(b)

vs = np.vstack((a,b))
print(vs)

# Task 8

hs = np.hstack((a,b))
print(hs)

# Task 9

arr = np.array([10,20,30,40,50,60])
print(np.split(arr,3))

# Task 10

a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[11,22,33,44]])
print(a)
hs = np.hsplit(a,2)
print(hs)

# Task 11

vs = np.vsplit(a,1)
print(vs)

# Task 12

a = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
ds = np.dsplit(a,2)
print(ds)

# Task 13

arr = np.array([10,20,30,40,50,60,70,80,90,100])
i = np.insert(arr,3,100)
print(i)

# Task 14

a = np.append(arr,999)
print(a)

# Task 15

d = np.delete(arr,0)
print(d)

d = np.delete(arr,-1)
print(d)

d = np.delete(arr,2)
print(d)

# Task 16

max = np.max(arr)
print(max)

min = np.min(arr)
print(min)

im = np.argmax(arr)
print(im)

imin = np.argmin(arr)
print(imin)

# Task 17

gr = np.where(arr>50)
print(gr)

# Task 18

arr = np.array([1,2,3,4,5,6,7,8,9,10,1,4,6,8,10])
even = np.where(arr % 2 == 0,"even","odd")
print(even)

# Task 19

values,counts = np.unique(arr,return_counts=True)
dup = values[counts>1]
print(dup)

# Task 20	

a = np.array([50,10,90,30,20])
s = np.sort(a)
print(s)

# Task 21

re = np.unique(arr)
print(re)

# Task 22

arr = np.array([10,20,30,40,50])
a = np.sum(arr)
print(a)

# Task 23

b = np.mean(arr)
print(b)

# Task 24

c = np.median(arr)
print(c)

# Task 25

d = np.std(arr)
print(d)

# Task 26

e = np.var(arr)
print(e)

# Task 27

f = np.cumsum(arr)
print(f)

# Task 28

g = np.cumprod(arr)
print(g)

# Task 29

arr = np.array([1,2,3,4])
f = arr.astype(float)
print(f)

s = arr.astype(str)
print(s)

b = arr.astype(bool)
print(b)