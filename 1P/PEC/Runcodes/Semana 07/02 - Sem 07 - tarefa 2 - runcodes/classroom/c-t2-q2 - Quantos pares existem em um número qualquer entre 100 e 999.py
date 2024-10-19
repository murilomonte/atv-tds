def contPar(num):
    qtPar = 0

    if num < 100:
        if (num // 10) % 2 == 0:
            qtPar += 1
            num = num % 10
            print(num)
        if (num // 1) % 2 == 0:
            qtPar += 1
    elif num <= 999:
        if (num // 100) % 2 == 0:
            qtPar += 1
            num = num % 100
        if (num // 10) % 2 == 0:
            qtPar += 1
            num = num % 10
        if (num // 1) % 2 == 0:
            qtPar += 1

    return qtPar

num = int(input('Insira um número entre 100 e 999: '))

print('Quantidade de números pares: ', contPar(num))