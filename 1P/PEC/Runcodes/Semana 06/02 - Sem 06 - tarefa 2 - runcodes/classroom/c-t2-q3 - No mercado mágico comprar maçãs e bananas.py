macas = float(input('Insira a quantidade de maçãs: '))
bananas = float(input('Insira quantidade de bananas: '))

def calcular(macas, bananas):
    totalB = bananas * 2
    totalM = macas * 3
    return totalB + totalM

print(f'Valor total: {calcular(macas, bananas)}')