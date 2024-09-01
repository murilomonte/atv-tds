def main():
    lista = []
    impares = []
    pares = []

    print('Insira 20 números: ')
    while len(lista) < 20:
        num = int(input('> ').strip())
        lista.append(num)
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    print('Todos os números: ', lista)
    print('Somente os pares: ', pares)
    print('Somente os impares: ', impares)     

if __name__ == '__main__':
    main()