Практическая работа № 13

import numpy as np
import matplotlib.pyplot as plt

X = [4, 5, 6, 7, 8, 8, 3, 9, 11, 13, 14, 14, 8, 5, 7, 12, 2, 1, 8]
print('Исходный массив X')
print(X)

N = len(X)

Y = [4, 5.5, 6, 6.5, 7, 9, 3, 8, 10, 12, 13, 14, 9, 6, 7, 11, 1, 1, 7]
print('Исходный массив Y')
print(Y)

Sx = sum(X)
Sy = sum(Y)
Sxx = np.dot(X,X)
Sxy = np.dot(X,Y)

a = (N * Sxy - Sx * Sy) / (N * Sxx - Sx * Sx)
b = (Sy - a * Sx) / N
print('y = ', a, '*x+', b)

YY = []

for x in X:
    YY.append(float(a * x + b))

Z = (np.array(Y) - np.array(YY))**2
SS = sum(Z)
print('SS = ', SS)

plt.title('MHK')
plt.xlabel('X')
plt.ylabel('Y')

plt.scatter(X,Y,c = 'r', marker = '*')

plt.plot(X, YY, 'b')

plt.show()
