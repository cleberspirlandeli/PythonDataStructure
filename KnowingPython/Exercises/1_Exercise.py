#1
#Ler dois números inteiros, executar e mostrar o resultado das seguintes operações: adição, subtração, multiplicação e divisão
n1 = int(input('Input the number 1:'))
n2 = int(input('Input the number 2:'))
print('Sum', n1+n2)
print('Sub', n1-n2)
print('Multiply', n1*n2)
print('Divide', n1/n2)

#2
# Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, utilizando um automóvel que faz 12 Km por litro.
# Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média durante ela. Desta forma,
# será possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE. Tendo o valor da distância,
# basta calcular a quantidade de litros de combustível utilizada na viagem, com a fórmula: LITROS_USADOS = DISTANCIA / 12.
# O programa deve apresentar os valores da velocidade média, tempo gasto na viagem, a distância percorrida e a quantidade
# de litros utilizada na viagem
time = int(input('Input the Time:'))
speed = int(input('Input the Speed:'))
distance = time * speed
gasoline_usage = distance / 12
print(f'Speed: {speed}km/h - Time: {time}hs - Distance: {distance}km - Gas Usage: {round(gasoline_usage, 2)}L')