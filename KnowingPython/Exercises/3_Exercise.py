# 1
# Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit.
# A fórmula de conversão é F = (9 * C + 160) / 5,
# na qual F é a temperatura em Fahrenheit e C é a temperatura em graus Celsius
# - Função para ler e retorna o valor da temperatura (não recebe parâmetro)
# - Função para fazer o cálculo (recebe como parâmetro a temperatura em graus Celsius)
# - Função para mostrar o resultado, recebendo como parâmetro o valor e fazendo a impressão

def inform_celsius():
    return float(input('Input the Celsius:'))

def calcule_celsius_to_fahrenheit(celsius=0):
    return (9 * celsius + 160) / 5

def print_fahrenheit(fahrenheit):
    print(f'Fahrenheit: {fahrenheit}')


celsius = inform_celsius()
fahrenheit = calcule_celsius_to_fahrenheit(celsius)
print_fahrenheit(fahrenheit)


# 2
# Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem,
# utilizando um automóvel que faz 12 Km por litro.
# Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média durante ela.
# Desta forma, será possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE.
# Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem, com a fórmula:
# LITROS_USADOS = DISTANCIA / 12.
# O programa deve apresentar os valores da velocidade média, tempo gasto na viagem,
# a distância percorrida e a quantidade de litros utilizada na viagem
# - Função para ler os valores (não recebe parâmetro e retorna os dois valores)
# - Função para calcular a distância (recebe como parâmetro o tempo e a velocidade e retorna a distância)
# - Função para calcular a quantidade de litros (recebe como parâmetro a distância e retorna os litros)
# - Função para apresentar o resultado (recebe como parâmetro os valores e somente imprime o resultado)
def inform_time_and_speed() -> (int, int):
    time = int(input('Input the Time:'))
    speed = int(input('Input the Speed:'))
    return time, speed

def CalcQuantityGasolineUsage(time:int=1, speed:int=100):
    distance = time * speed
    gasoline_usage = distance / 12
    print(f'Speed: {speed}km/h - Time: {time}hs - Distance: {distance}km - Gas Usage: {round(gasoline_usage, 2)}L')


time, speed = inform_time_and_speed()
CalcQuantityGasolineUsage()
CalcQuantityGasolineUsage(time, speed)
CalcQuantityGasolineUsage(1, 100)
CalcQuantityGasolineUsage(2, 110)