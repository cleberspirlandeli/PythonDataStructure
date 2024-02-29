# Operador condicional

if 5 > 3:
  print('5 é maior que 3')
print('teste')

if 5 > 3:
  print('5 é maior')
else:
  print('5 não é maior')

n = 9
if n == 4:
  print('n é igual a 4')
else:
  if n == 3:
    print('n é igual a 3')
  else:
    print('n não é igual a 4 nem 3')


a = 1
b = 5
if (a > 1) or (b % 2 == 0):
  print('a é maior que 1 e b é par')
else:
  print('Uma ou nenhuma das condições foram satisfeitas')


x = 2
y = 10
if (x > 1) or (y % 2 == 0):
  print('x é maior que 1 e y é par')
else:
  print('Uma ou nenhuma das condições foram satisfeitas')