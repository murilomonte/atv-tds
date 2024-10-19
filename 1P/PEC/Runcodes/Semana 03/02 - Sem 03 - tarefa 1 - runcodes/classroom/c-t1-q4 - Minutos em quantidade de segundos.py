segundos = int(input('Informe a quantidade de segundos: '))

minutos = int(segundos // 60)
restante = int(segundos % 60)

print(f'{segundos} segundos são {minutos} minutos e {restante} segundos')