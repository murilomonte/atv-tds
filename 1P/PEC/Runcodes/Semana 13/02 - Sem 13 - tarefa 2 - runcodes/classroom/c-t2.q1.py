def multiplica_constante(lista, constante):
    listaMult = []
    for valor in lista:
        listaMult.append(valor * constante)
    return listaMult

def main():
    lista = []
    print('Insira um valor (use 0 para parar):')
    while True:
        num = int(input('> ').strip())
        if num == 0: break
        lista.append(num)
    
    constante = int(input('Informe uma constante: ').strip())

    print('Todos os números da lista multiplicados pela constante são:\n', multiplica_constante(lista, constante))

if __name__ == '__main__':
    main()