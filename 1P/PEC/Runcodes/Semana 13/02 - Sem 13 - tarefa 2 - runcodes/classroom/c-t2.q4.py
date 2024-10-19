def soma_cumulativa(lista):
    listaSoma = []
    indice = 0
    soma = 0

    for valor in lista:
        indiceBkp = indice
        while True:
            soma += lista[indice]
            if indice == 0: break
            indice -= 1
        listaSoma.append(soma)
        soma = 0
        indice = indiceBkp + 1
    return listaSoma

def main():
    lista = []

    print('Insira valores para uma lista (use 0 para parar):')
    while True:
        num = int(input('> ').strip())
        if num == 0: break
        lista.append(num)
    
    print('A lista com a soma cumulativa:', soma_cumulativa(lista))

if __name__ == '__main__':
    main()
