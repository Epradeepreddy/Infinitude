import numpy as p
#by passing lists
"""
arr=p.array([1,2,3,4])

print(arr)

print(type(arr))


arr = p.array((1,2,3,4))

print(arr)

#0-D Arrays
arr =p.array(3)
print(arr)
#1-D Array

arr =p.array([1,2,3,4])
print(arr)

#2-D Array

arr =p.array([[1,2,3,4],[5,6,7,8]])
print(arr)

#3-D Array

arr = p.array([[[1,2,3,4],[5,6,7,8]],[[8,7,5,4],[3,2,1,6]]])
print(arr)

#Higher Dimensional arrays

arr =p.array([1,2,3,4],ndmin=5)
print(arr)
print(arr.ndim)



arr =p.array([1,2,3,4])
print(arr.dtype)


arr =p.array([[1.,2.,3.],[4.,5.,6.]])
res= arr ** 0.5
print(res)

#Basic indexing and slicing

#indexing a one-dimensional array

arr = p.arange(0,10)
print(arr)


#indexing a two-dimensional array

arr = p.arange(15).reshape(3,5)
print(arr)


arr=p.array([1,2,3,4,5,6,7])
print(arr[0])
print(arr[1:5])
print(arr[4:])
print(arr[::4])
print(arr[:4:])

#negative slicing
arr = p.array([1,2,3,4,5,6,7])
print(arr[-3:-1])

arr=p.array([1,2,3,4,5])
print(arr[::-3])


#step slicing
arr = p.array([1,2,3,4,5,6,7])
print(arr[1:5:2])
print(arr[::2])

#slicing 2-D Array

arr=p.array([[1,2,3,4,5],[3,6,7,8,9]])
print(arr[1,1:4])

arr = p.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[0:2,2])

#Boolean Indexing

a=p.array([1,2,3,4])
b=p.array([True,True,False,True])
c=a[b]

print(c)

#Fancy Indexing

a=p.arange(1,10)
print(a)
index=p.array([2,3,4,5])
print(a[index])


arr = p.arange(0,10).reshape(2,5)
print(arr)

arr =p.array([1,2,3,4],dtype=float,ndmin=5)
arr1=p.random.rand(3,2)
print(arr1)
"""





