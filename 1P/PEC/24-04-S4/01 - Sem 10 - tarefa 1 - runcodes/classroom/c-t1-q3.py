def main ():
    quantidade = 0
    for i in range(100):
        entrada = int(input('Digite um número: '))
        quantidade += entrada
    print(f'A média dos números é: {quantidade/100:.2f}')


if __name__ == "__main__":
    main()