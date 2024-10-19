def main():
    lista = []
    print('Insira 10 números:')
    while True:
        num = int(input('> ').strip())
        lista.append(num)
        if len(lista) == 10: break

    soma = 0
    multiplicacao = 1
    for valor in lista:
        soma += valor
        multiplicacao *= valor
    
    print('Todos os números:', lista)
    print('Todos somados:', soma)
    print('Todos multiplicados', multiplicacao)

if __name__ == '__main__':
    main()