def ePar(num):
    impar = 0
    par = 0
    if num % 2 == 0:
        par = 1
        return par, impar
    else:
        impar = 1
        return par, impar

def main ():
    impares = 0
    pares = 0
    for i in range(100):
        entrada = int(input().strip())
        par, impar = ePar(entrada)
        pares += par
        impares += impar
    print(pares)
    print(impares)


if __name__ == "__main__":
    main()