def main():
    lista = []

    while len(lista) < 100:
        num = int(input().strip())
        lista.append(num)
    
    lista.sort()

    listaMult = []
    indice = 0
    for valor in lista:
        if indice % 2 == 0:
            valor *= 3
            listaMult.append(valor)
        else:
            valor *= 5
            listaMult.append(valor)
        indice += 1
    print(listaMult)

if __name__ == '__main__':
    main()
