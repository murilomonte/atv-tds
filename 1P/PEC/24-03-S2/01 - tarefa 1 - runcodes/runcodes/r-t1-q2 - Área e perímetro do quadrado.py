lado = float(input('').strip())

def area(lado):
    return lado ** 2

def perimetro(lado):
    return 4 * lado

print(f'{area(lado):10.4f}')
print(f'{perimetro(lado):10.4f}')