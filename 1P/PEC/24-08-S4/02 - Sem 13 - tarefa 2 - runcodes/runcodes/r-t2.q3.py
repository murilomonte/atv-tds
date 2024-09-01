def main():
    lista = []

    while len(lista) < 50:
        num = float(input().strip())
        lista.append(num)
    
    listaAprovados = []
    indice = 0
    for valor in lista:
        if valor >= 6:
            listaAprovados.append(indice)
        indice += 1
    print(listaAprovados)

if __name__ == '__main__':
    main()
