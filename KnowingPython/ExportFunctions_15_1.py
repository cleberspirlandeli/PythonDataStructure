def somar(a: int, b: int) -> int:
    return a + b


def multiplicar(a: int, b: int) -> int:
    return a * b


def isPalindromo(text) -> bool:
    '''
    :param string: Texto a comparar, exemplo AMA
    :return: True ou False
    '''
    if text == text[::-1]:
        return True
    else:
        return False


def getInputTypeInt(text: str) -> int:
    return int(input(f"Input the '{text}':"))


def getInputTypeFloat(text: str) -> float:
    return round(float(input(f"Input the '{text}':")), 2)


def getInputTypeString(text: str) -> str:
    return input(f"Input the '{text}':")
