minutos = int(input('Quantos minutos?: '))

def calcMinutos(minutos):
    horas = minutos // 60
    minutosRes = minutos % 60
    return horas, minutosRes

horas, minutosRes = calcMinutos(minutos)
print(f'São: {horas}:{minutosRes}')

