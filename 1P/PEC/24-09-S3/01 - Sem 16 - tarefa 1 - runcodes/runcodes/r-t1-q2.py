def lerMeses():
    meses = []

    for mes in range(1, 13):
        temperatura = float(input())
        escala = str(input().upper()[0])
        meses.append([
            mes,
            temperatura,
            escala
        ])
    return meses

def mesesExtenso(mes):
    if mes == 1: return 'Janeiro'
    if mes == 2: return 'Fevereiro'
    if mes == 3: return 'Março'
    if mes == 4: return 'Abril'
    if mes == 5: return 'Maio'
    if mes == 6: return 'Junho'
    if mes == 7: return 'Julho'
    if mes == 8: return 'Agosto'
    if mes == 9: return 'Setembro'
    if mes == 10: return 'Outubro'
    if mes == 11: return 'Novembro'
    if mes == 12: return 'Dezembro'
    return 'Mês inválido'

def conversor(temperatura, escala):
    if escala.upper() == 'F':
        return round((temperatura - 32) * 5/9 + 273.15, 2)
    if escala.upper() == 'C':
        return round(temperatura + 273.15, 2)
    if escala.upper() == 'K':
        return temperatura

def converter(meses):
    convertidos = []
    for info in meses:
        convertidos.append([
            info[0],
            conversor(info[1], info[2])
        ])
    return convertidos

def mediaAnual(meses):
    soma = 0
    for mediaMensal in meses:
        soma += mediaMensal[1]
    return soma / len(meses)

def compara(mediaAnual, meses):
    maiores = []
    for mediaMensal in meses:
        if mediaMensal[1] > mediaAnual:
            maiores.append([
                mediaMensal[0],
                mediaMensal[1]
            ])

    print(f'TEMPERATURA MÉDIA ANUAL\n{round(mediaAnual, 2)}K')
    print('TEMPERATURAS ACIMA DA MÉDIA ANUAL:')
    for maior in maiores:
        print(f'{mesesExtenso(maior[0])}: {round(maior[1], 2)}K')

def main():
    meses = lerMeses()
    meses = converter(meses)
    mediaA = mediaAnual(meses)
    compara(mediaA, meses)


if __name__ == "__main__":
    main()
