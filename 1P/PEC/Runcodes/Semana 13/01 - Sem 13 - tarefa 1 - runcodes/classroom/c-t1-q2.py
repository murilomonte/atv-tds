def main():
    lista = []
    num = int(input('Insira a quantiade de números: ').strip())

    # Preencha com 0 (zero) e imprima a lista;
    while len(lista) < num:
        lista.append(0)
    print('Lista com 0:\n', lista)

    # b - preencha com os números de 1 a n e imprima a lista;
    lista = []
    contador = 1
    while len(lista) < num:
        lista.append(contador)
        contador += 1
    print(f'Todos os números de 1 até {num}\n', lista)

    # c - preencha com valores inteiros lidos pelo teclado e imprima a lista;
    lista = []
    print('Digite', num, 'numeros.')
    while len(lista) < num:
        lista.append(int(input('> ')))
    print('Uma lista com todos eles', lista)

    # d - preencha na ordem inversa com valores inteiros lidos pelo teclado e imprima a lista; dica: use insert
    lista = []
    print('Digite', num, 'numeros.')
    while len(lista) < num:
        lista.insert(0, int(input('> ').strip()))
    print('Eles invertidos:', lista)

if __name__ == '__main__':
    main()