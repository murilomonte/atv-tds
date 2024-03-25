tempo = int(input('Insira a quantidade de tempo: '))

def calcSegundos(tempo):
    horas = tempo // 3600
    segTotal = tempo % 3600
    minutos = segTotal // 60
    segRes = segTotal % 60
    return f'{horas}:{minutos}:{segRes}'

print(calcSegundos(tempo))