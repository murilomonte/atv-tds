raio = float(input('').strip())

PI = 3.141592
circunferencia = 2 * PI * raio
areaEsfera = 4 * PI * (raio ** 2)
areaCirculo = PI * (raio ** 2)
volumeEsfera = 4 / 3 * PI * (raio ** 3)

print(f'{circunferencia:.6f}')
print(f'{areaCirculo:.6f}')
print(f'{areaEsfera:.6f}')
print(f'{volumeEsfera:.6f}')