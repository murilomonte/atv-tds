a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))

def calcular(a, b, c):
    return 2 * a + 5 * b - c

print(f'O resultado é {calcular(a, b, c)}')