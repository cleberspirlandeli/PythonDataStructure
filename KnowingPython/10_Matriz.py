import numpy as np

matriz = np.array([[1, 2, 3],
                   [4, 5, 6]])
print(matriz) # array([[1, 2, 3],
              #        [4, 5, 6]])

print(matriz.shape) # (2, 3) -> 2 Lines - 3 Columns

print(matriz[0]) # array([1, 2, 3])

print(matriz[1]) # array([4, 5, 6])

print(matriz[0][0]) # 1
print(matriz[0][1]) # 2
print(matriz[0][2]) # 3

print(matriz[1][0]) # 4
print(matriz[1][1]) # 5
print(matriz[1][2]) # 6

for i in range(matriz.shape[0]):
  print(matriz[i])
  for j in range(matriz.shape[1]):
    print(matriz[i][j])