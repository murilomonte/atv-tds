def lerMatriz():
    matriz = []
    listaIn = []

    tamanho = int(input().strip())

    for coluna in range(tamanho):
        for linha in range(tamanho):
            listaIn.append(
                int(input().strip())
            )
        matriz.append(listaIn)
        listaIn = []
    return matriz

def maiorMenorPos(matriz):
    maior = menor = matriz[0][0]
    maiorPos = [0, 0]
    menorPos = [0, 0]

    for colInd, linha in enumerate(matriz):
        for listInd, elemento in enumerate(linha):
            if elemento > maior:
                maior = elemento
                maiorPos.clear()
                maiorPos.extend([colInd, listInd])
            
            if elemento < menor:
                menor = elemento
                menorPos.clear()
                menorPos.extend([colInd, listInd])

    return tuple(maiorPos), tuple(menorPos)
            
def main():
    matriz = lerMatriz()
    print(maiorMenorPos(matriz)[0])
    print(maiorMenorPos(matriz)[1])

if __name__ == "__main__":
    main()