macas = float(input('').strip())
bananas = float(input('').strip())

def calcular(macas, bananas):
    totalB = bananas * 2
    totalM = macas * 3
    return totalB + totalM

print(f'{calcular(macas, bananas):.2f}')