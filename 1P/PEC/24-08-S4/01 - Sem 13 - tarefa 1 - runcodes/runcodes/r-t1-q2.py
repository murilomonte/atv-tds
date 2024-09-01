def main():
    lista = []
    num = int(input().strip())

    # Preencha com 0 (zero) e imprima a lista;
    while len(lista) < num:
        lista.append(0)
    print(lista)

    # b - preencha com os números de 1 a n e imprima a lista;
    lista = []
    contador = 1
    while len(lista) < num:
        lista.append(contador)
        contador += 1
    print(lista)

    # c - preencha com valores inteiros lidos pelo teclado e imprima a lista;
    lista = []
    while len(lista) < num:
        lista.append(int(input()))
    print(lista)

    # d - preencha na ordem inversa com valores inteiros lidos pelo teclado e imprima a lista; dica: use insert
    lista = []
    while len(lista) < num:
        lista.insert(0, int(input().strip()))
    print(lista)

if __name__ == '__main__':
    main()