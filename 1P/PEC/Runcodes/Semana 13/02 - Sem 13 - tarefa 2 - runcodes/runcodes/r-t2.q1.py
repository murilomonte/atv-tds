def multiplica_constante(lista, constante):
    listaMult = []
    for valor in lista:
        listaMult.append(valor * constante)
    return listaMult

def main():
    lista = []

    while True:
        num = int(input().strip())
        if num == 0: break
        lista.append(num)
    
    constante = int(input().strip())

    print(multiplica_constante(lista, constante))

if __name__ == '__main__':
    main()