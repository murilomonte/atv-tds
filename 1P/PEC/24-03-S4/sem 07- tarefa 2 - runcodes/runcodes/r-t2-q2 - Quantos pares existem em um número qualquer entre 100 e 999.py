def contPar(num):
    qtPar = 0

    if num < 100:
        if (num // 10) % 2 == 0:
            qtPar += 1
            num = num % 10
        if (num // 1) % 2 == 0:
            qtPar += 1
    else:
        if (num // 100) % 2 == 0:
            qtPar += 1
            num = num % 100
        if (num // 10) % 2 == 0:
            qtPar += 1
            num = num % 10
        if num % 2 == 0:
            qtPar += 1

    return qtPar

num = int(input('').strip())

print(contPar(num))