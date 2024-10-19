minutos = int(input('').strip())

horas = minutos // 60
minutosRestantes = minutos % 60

print(f'{horas}h{minutosRestantes}min')