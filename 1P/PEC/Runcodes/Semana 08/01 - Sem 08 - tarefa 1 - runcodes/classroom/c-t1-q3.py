def maiorNum(n1, n2, n3, n4, n5):
    maior = n1
    if n2 > maior:
        maior = n2
    if n3 > maior:
        maior = n3
    if n4 > maior:
        maior = n4
    if n5 > maior:
        maior = n5
    return maior

def menorNum(n1, n2, n3, n4, n5):    
    menor = n1
    if n2 < menor:
        menor = n2
    if n3 < menor:
        menor = n3
    if n4 < menor:
        menor = n4
    if n5 < menor:
        menor = n5
    return menor

def main():
    n1 = int(input('Insira o primeiro número: '))
    n2 = int(input('Insira o segundo número: '))
    n3 = int(input('Insira o terceiro número: '))
    n4 = int(input('Insira o quarto número: '))
    n5 = int(input('Insira o quinto número: '))

    print(maiorNum(n1, n2, n3, n4, n5))
    print(menorNum(n1, n2, n3, n4, n5))
    
if __name__ == '__main__':
    main()