def main():
    lista = []
    while True:
        num = int(input().strip())
        lista.append(num)
        if len(lista) == 10: break

    soma = 0
    multiplicacao = 1
    for valor in lista:
        soma += valor
        multiplicacao *= valor
    
    print(lista)
    print(soma)
    print(multiplicacao)

if __name__ == '__main__':
    main()