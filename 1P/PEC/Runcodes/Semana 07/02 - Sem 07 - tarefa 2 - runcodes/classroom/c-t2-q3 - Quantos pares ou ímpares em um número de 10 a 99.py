def contParImp(num):
    qtImp = 0

    if num < 100:
        if not (num // 10) % 2 == 0:
            qtImp += 1
            num = num % 10
        if not (num // 1) % 2 == 0:
            qtImp += 1

    return qtImp

num = int(input('Insira um número de 10 a 99: '))

qtImp = contParImp(num)

if qtImp == 2:
    print('Os dois dígitos são ímpares.')
elif qtImp == 1:
    print('Apenas um dígito é ímpar.')
else:
    print('Nenhum dígito é ímpar.')
