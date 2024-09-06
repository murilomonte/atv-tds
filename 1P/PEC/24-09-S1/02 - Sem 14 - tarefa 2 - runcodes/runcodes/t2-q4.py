def escalar(listaX, listaY):
    resultado = 0
    conta = ''
    for indice in range(len(listaY)):
        resultado += listaX[indice] * listaY[indice]
        conta += f'({listaX[indice]} x {listaY[indice]})'
        if indice < len(listaY) - 1:
            conta += ' + '
    conta += f' = {resultado}'
    return conta
            
        
def main():
    listaX = []
    listaY = []

    while len(listaY) + len(listaY) < 10:
        num = int(input().strip())
        if len(listaX) < 5:
            listaX.append(num)
        else:
            listaY.append(num)
    print(listaX)
    print(listaY)
    print(escalar(listaX, listaY))

if __name__ == '__main__':
    main()