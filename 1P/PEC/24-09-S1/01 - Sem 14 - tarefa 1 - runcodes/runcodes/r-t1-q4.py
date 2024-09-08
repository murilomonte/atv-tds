def maior(alturas):
    maiorAltura = alturas[0]
    alturaIndice = 0
    for indice in range(len(alturas)):
        if alturas[indice] > maiorAltura:
            maiorAltura = alturas[indice]
            alturaIndice = indice
    return alturaIndice

def media(alturas):
    return (sum(alturas)) / len(alturas)

def maiorMedia(alturas, media):
    maioresLista = []
    for indice in range(len(alturas)):
        if alturas[indice] >= media:
            maioresLista.append(indice)
    return maioresLista

def main():
    nomes = []
    alturas = []

    while len(nomes) < 12:
        nome = str(input().strip())
        nomes.append(nome)
        altura = float(input().strip())
        alturas.append(altura)
    
    print('JOGADOR MAIS ALTO DO TIME')
    print(nomes[maior(alturas)])
    print(f'{alturas[maior(alturas)]:.2f}')

    print('ALTURA MÉDIA DO TIME')
    mediaTime = media(alturas)
    print(f'{mediaTime:.2f}')

    print('JOGADORES MAIS ALTOS QUE A MÉDIA DO TIME')
    maioresMedia = maiorMedia(alturas, mediaTime)
    for indice in maioresMedia:
        print(nomes[indice])
        print(f'{alturas[indice]:.2f}')


if __name__ == '__main__':
    main()