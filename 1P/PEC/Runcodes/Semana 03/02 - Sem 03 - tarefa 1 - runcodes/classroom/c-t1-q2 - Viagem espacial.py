distancia = int(input('Qual a distância do planeta? (em Km): '))
velocidade = int(input('Qual a velocidade da nave? (em Km/h): '))

tempo = distancia // velocidade
dias = int(tempo // 24)
horas = int(tempo % 24)

print(f'Nessa velocidade você irá chegar em {dias} dias e {horas} horas')
