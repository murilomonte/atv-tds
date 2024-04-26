def main ():
    maior = 0
    for i in range(100):
        entrada = int(input().strip())
        if entrada > maior:
            maior = entrada

    print(maior)

if __name__ == "__main__":
    main()