def main():
    listaA = []
    listaB = []
    listaC = []

    while len(listaA) + len(listaB) < 50:
        valor = int(input().strip())
        if len(listaA) < 25:
            listaA.append(valor)
        elif len(listaB) < 25:
            listaB.append(valor)
        else:
            continue
    
    indice = 0
    while len(listaC) < 50:
        listaC.append(listaA[indice])        
        listaC.append(listaB[indice])
        indice += 1
    
    print(listaA)
    print(listaB)
    print(listaC)      

if __name__ == '__main__':
    main()