for numero in range(1, 6):
  print(numero)

for numero in range(5, 0, -1):
  print(numero)


soma = 0
for numero in range(1, 6):
  soma = soma + numero
  #print(soma)

print(soma)


palavra = 'sorvete'
for letra in palavra:
  #print(letra)
  if letra == 'v':
    print('Achou a letra v')



for i in range(0,5):
  print(i)
  print('---')
  for j in range(0,3):
    print(j)
  print()