lado = float(input('Qual o tamanho do lado do quadrado?: '))

def area(lado):
    return lado ** 2

def perimetro(lado):
    return 4 * lado

print(f'A área do quadrado é igual a {area(lado):10.4f}')
print(f'O perimetro do quadrado é igual a {perimetro(lado):10.4f}')