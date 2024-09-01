def main():
    lista = []
    impares = []
    pares = []

    while len(lista) < 20:
        num = int(input().strip())
        lista.append(num)
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    print(lista)
    print(pares)
    print(impares)     

if __name__ == '__main__':
    main()