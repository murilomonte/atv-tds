minutos = int(input('').strip())

def calcMinutos(minutos):
    horas = minutos // 60
    minutosRes = minutos % 60
    return horas, minutosRes

horas, minutosRes = calcMinutos(minutos)
print(f'{horas}:{minutosRes}')

