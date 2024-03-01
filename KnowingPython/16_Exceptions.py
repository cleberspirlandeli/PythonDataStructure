#NameError: variável nao foi definida
#TypeError: tipos de dados incompatíveis
#RuntimeError: erro de execução
#SyntaxError: sintaxe digitada é inválida e não reconhecida pelo interpretador
#ZeroDivisionError: divisão por zero
#IndexError: índice está fora da coleção

#SyntaxError -> can't assign to literal
3 = 4

#NameError -> name 'nome' is not defined
print('Meu nome é', nome)

#ZeroDivisionError -> division by zero
print(3 / 0)

#TypeError -> unsupported operand type(s) for /: 'float' and 'str'
2.3 / 'aaa'


#IndexError -> list index out of range
c = [1,2,3,4,5]
c[10]


try:
  n = int(input('Digite um número inteiro: '))
except:
  print('Valor inválido')
else:
  print(f'Valor digitado é {n}')


while True:
  try:
    n = int(input('Digite um número inteiro: '))
  except:
    print('Valor inválido')
  else:
    print(f'Valor digitado é {n}')
    break


while True:
  try:
    p = int(input('Digite um número inteiro'))
  except ValueError:
    print('Valor inválido')
  except KeyboardInterrupt:
    print('Usuário interrompeu a execução')
    break
  else:
    print(f'Valor digitado é {p}')
    break