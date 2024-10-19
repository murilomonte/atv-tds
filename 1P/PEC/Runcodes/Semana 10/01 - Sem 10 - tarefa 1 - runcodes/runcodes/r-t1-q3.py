def main ():
    quantidade = 0
    for i in range(100):
        entrada = int(input().strip())
        quantidade += entrada
    print(f'{quantidade/100:.2f}')


if __name__ == "__main__":
    main()