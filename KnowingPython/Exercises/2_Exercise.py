# 1
# Lista:
# Crie uma estrutura de repetição para fazer a leitura de 5 números inteiros e os armazene dentro de uma lista.
# Após a leitura, crie outra estrutura de repetição para somar todos os valores digitados
numberList = []
for i in range(0, 5): # for _ in range(0, 5)
    value = int(input(f'Set a number {i+1}: '))
    numberList.append(value)

total1 = 0
for number in numberList:
    total1 += number

print(f'Total: {total1}')

# Other format
# for number in range(len(numberList))
#   total1 += number

# Other format
# import numpy as np
# np.array(numberList).sum()


# 2
# Dicionário:
# Crie um dicionário para armazenar o nome e a nota de 3 alunos, fazendo a leitura dos valores por meio de uma
# estrutura de repetição.
# Depois, crie uma nova estrutura de repetição para somar todas as notas e retornar a média
dictionary = {}
for i in range(0, 3):
    name = input(f'{i+1} - Set a name: ')
    grade = int(input(f'{i+1} - Set a grade: '))
    dictionary[name] = grade

total2 = 0
for grade in dictionary.values():
    total2 += grade

print(f'Total: {total2 / len(dictionary)}')


# 3
# Matriz: Dada a matriz abaixo, construa uma estrutura de repetição para percorrer e somar todos os elementos da matriz
# matriz = np.array([[3, 4, 1],
#                   [3, 1, 5]])
import numpy as np
matriz = np.array([[3, 4, 1],
                   [3, 1, 5]])

print('LEN', len(matriz)) # 2
print('SIZE', matriz.size) # 6

total3 = 0
for i in range(matriz.shape[0]):
  for j in range(matriz.shape[1]):
    total3 += matriz[i][j]

print(f'Total: {total3}') # Total: 17
