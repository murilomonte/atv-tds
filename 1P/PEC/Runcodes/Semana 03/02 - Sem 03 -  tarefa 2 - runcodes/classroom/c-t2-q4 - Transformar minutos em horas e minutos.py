minutos = int(input('Informe a quantidade de minutos: '))

horas = minutos // 60
minutosRestantes = minutos % 60

print(f'{minutos} minutos são equivalentes a: {horas}h{minutosRestantes}min')