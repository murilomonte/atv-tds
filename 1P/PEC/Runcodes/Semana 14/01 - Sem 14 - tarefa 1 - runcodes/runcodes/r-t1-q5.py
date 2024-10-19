def filtroIdade(idades):
    maiores = []
    for indice in range(len(idades)):
        if idades[indice] > 13:
            maiores.append(indice)
    return maiores

def media(alturas):
    return (sum(alturas)) / len(alturas)

def main():
    nomes = []
    alturas = []
    idades = []

    while len(nomes) < 30:
        nome = str(input().strip())
        nomes.append(nome)

        idade = int(input().strip())
        idades.append(idade)

        altura = float(input().strip())
        alturas.append(altura)

    print('MAIORES DE 13 ANOS COM ALTURA ABAIXO DA MÉDIA')
    idadeFiltradas = filtroIdade(idades)
    alturaMedia = round(media(alturas), 2)
    for indice in idadeFiltradas:
        if alturas[indice] < alturaMedia:
            print(nomes[indice])

if __name__ == '__main__':
    main()