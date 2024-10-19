distancia = int(input('').strip())
velocidade = int(input('').strip())
tempo = distancia // velocidade
dias = int(tempo // 24)
horas = int(tempo % 24)

print(f'{dias} dias e {horas} horas')
