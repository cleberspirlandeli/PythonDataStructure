#Operadores lógicos
a = True
b = False

print(a, b)
print(f'a == 1 - {a == 1} --- a == 0 - {a == 0}')
print(f'b == 1 - {b == 1} --- b == 0 - {b == 0}')
print('')
print(f'1- {a and b}')
print(f'2- {a & b}')
print(f'3- {a or b}')
print(f'4- {a | b}')

c = a and b
print("\n'A' e 'B' são iguais é", c)

d = a or b
print("\n'A' ou 'B' é igual a", d)

print('')
print(f"Value 'a' - {a} - Not Value 'a' - {not a}")
print(f"Value 'b' - {b} - Not Value 'b' - {not b}")

#Operadores relacionais
print(f"Maior {5 > 3}")
print(f"Maior Igual {5 >= 3}")
print(f"Menor {5 < 3}")
print(f"Menor Igual {5 <= 3}")
print(f"Igual {5 == 3}")
print(f"Diferente {5 != 3}")

