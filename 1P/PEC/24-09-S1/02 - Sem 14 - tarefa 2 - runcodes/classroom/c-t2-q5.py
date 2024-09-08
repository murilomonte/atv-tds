def merge(listaX, listaY):
    listaZ = []
    for indice in range(len(listaY)):
        if listaX[indice] not in listaZ: listaZ.append(listaX[indice])
    for indice in range(len(listaX)):
        if listaY[indice] not in listaZ: listaZ.append(listaY[indice])
    return listaZ
        
def main():
    listaX = []
    listaY = []

    print('Insira 10 números em cada lista: ')
    while len(listaY) + len(listaY) < 20:
        num = int(input('> ').strip())
        if len(listaX) == 9 and len(listaY) == 0: print('Lista X completa. Insira os valores da lista Y')
        if len(listaX) < 10:
            listaX.append(num)
        else:
            listaY.append(num)
    print('Listas mescladas, desconsiderando números repetidos:')
    print(merge(listaX, listaY))

if __name__ == '__main__':
    main()