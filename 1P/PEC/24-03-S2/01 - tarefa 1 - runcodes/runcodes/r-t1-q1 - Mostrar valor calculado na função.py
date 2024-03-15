a = int(input('').strip())
b = int(input('').strip())
c = int(input('').strip())

def calcular(a, b, c):
    return 2 * a + 5 * b - c

print(f'{calcular(a, b, c)}')