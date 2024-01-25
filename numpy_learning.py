import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# # The Basics
#
# a = np.array([1, 2, 3])
# print(a)
#
# b = np.array([[9.0, 10.0, 6.0], [2.0, 1.0, 1.0]])
# print(b)
#
# # get dimension
# print(a.ndim)
# print(b.ndim)
#
# # get shape
# print(a.shape)
# print(b.shape)
#
# # get type
# print(a.dtype)
# print(b.dtype)
# # get size
# print(a.size)
# print(b.size)
# print(a.itemsize) # 4
# print(b.itemsize) # 8
# print(b.itemsize * b.size) # b.nbytes
#
# c = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
#
# print(c[0, 1, 1])
# print(c[:, :, 1])
#
# # random integer values
# print(np.random.randint(10, size=(3, 3)))
#
# a = np.array([1,2,3,4])
# print(a)
# print(a*2)
# print(a-2)
# print(a**2)
#
# e = np.arange(20, 100, 3)
# print(e)
#
# e = np.random.rand(10)
# print(e)

# a = np.array((1, 2, 3))
# b = np.array((4, 5, 6))
# print(np.hstack((a, b)))
# print(np.vstack((a, b)))
# a = np.array([[1, 2, 3], [4, 5, 6]])
# b = np.array([[4, 5, 6], [7, 8, 9]])
# print(a)
# print(b)
# print(np.hstack((a, b)))
# print(np.vstack((a, b)))

A = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(A)
print(A.values)
print(A.index)

marks_dict = {'A': 85, 'B': 75, 'C': 65, 'D': 55}
print(marks_dict)
marks = pd.Series(marks_dict)
print(marks)
print(marks['A'])
print(marks[0:3])

grades_dict = {'A': 4.0, 'B': 3.5, 'C': 3.0, 'D': 2.5}
grades = pd.Series(grades_dict)

B = pd.DataFrame({'Marks': marks, 'Grades': grades})
print(B)

B['ScaledMarks'] = 100*(B['Marks']/90)
print(B)

del B['ScaledMarks']
print(B)

print(B[B['Marks'] > 70])

x = np.linspace(0, 10, num=1000)
y = np.sin(x)
plt.plot(x, y)
plt.show()
plt.scatter(x, y)
plt.show()
