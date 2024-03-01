def message1():
    print('Text for the function')


message1()
message1()
message1()


def message2(text):
    print(text)


message2('text 1')
message2('text 2')
message2('text 3')


def sum1(a, b):
    print('sum1', a + b)


sum1(10, 20)


def sum2(a, b):
    return a + b


print('sum2', sum2(1, 2))
result = sum2(3, 4)
print('Result:', result)


def calcula_energia_potencial_gravitacional(m, h, g=10):
    '''
  Calcula a energia potencial gravitacional
  Argumentos:
  m: massa, entrada como uma variável float
  h: altura, entrada como uma variável float

  Argumento opcional:
  g: aceleração gravitacional, com valor default de 10
  '''
    e = g * m * h
    print(e)
    return e


calcula_energia_potencial_gravitacional(30, 12) # 3600
calcula_energia_potencial_gravitacional(30, 12, 9.8) # 3528.0
help(calcula_energia_potencial_gravitacional)