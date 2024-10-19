def filtro(lista):
    quantidade = 0
    soma = 0
    for numero in lista:
        if numero < 0: quantidade += 1
        else: soma += numero
    return quantidade, soma

def main():
    lista = []
    print('Insira 10 números reais:')
    while len(lista) < 10:
        num = int(input('> ').strip())
        lista.append(num)

    print('Lista completa:', lista)
    print('Quantidade de números negativos: ', filtro(lista)[0])
    print('Soma dos positivos:', filtro(lista)[1])
    

if __name__ == '__main__':
    main()