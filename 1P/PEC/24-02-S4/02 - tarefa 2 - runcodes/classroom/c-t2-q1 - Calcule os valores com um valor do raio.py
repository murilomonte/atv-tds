raio = float(input('Informe o raio do circulo: '))

PI = 3.141592
circunferencia = 2 * PI * raio
areaEsfera = 4 * PI * (raio ** 2)
areaCirculo = PI * (raio ** 2)
volumeEsfera = 4 / 3 * PI * (raio ** 3)

print(f'O comprimento da circunferencia é: {circunferencia:.6f}')
print(f'A área do circulo é: {areaCirculo:.6f}')
print(f'A área da esfera é: {areaEsfera:.6f}')
print(f'O volume da esfera é: {volumeEsfera:.6f}')