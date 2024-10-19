def main():
    quantidade = int(input().strip()) - 3

    sequencia = '0, 1, 1'
    contagem = 0

    fib = 0
    n1 = 1
    n2 = 1

    while contagem < quantidade:
        fib = n1 + n2
        n2 = n1
        n1 = fib

        sequencia += f', {fib}'
        contagem += 1

    print(sequencia)

if __name__ == '__main__':
    main()