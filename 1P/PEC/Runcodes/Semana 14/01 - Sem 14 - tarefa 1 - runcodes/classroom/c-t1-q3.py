def contador(lista, num):
    contador = 0
    for dado in lista:
        if dado == num: contador += 1
    return contador

def main():
    listaA = []
    listaB = []
    listaC = []

    print('Insira 20 números para a Lista A')
    while len(listaA) + len(listaB) < 40:
        num = int(input('> ').strip())
        if len(listaA) == 20 and len(listaB) == 0: 
            print('Lista A completa.')
            print('Insira 20 números para lista B.')
        if len(listaA) < 20: listaA.append(num)
        else: listaB.append(num)    

    indice = 0
    while len(listaC) < len(listaA):
        listaC.append(listaA[indice] + listaB[indice])
        indice += 1
    print('Lista A:', listaA)
    print('Lista B:', listaB)
    print('Lista C:', listaC)

if __name__ == '__main__':
    main()