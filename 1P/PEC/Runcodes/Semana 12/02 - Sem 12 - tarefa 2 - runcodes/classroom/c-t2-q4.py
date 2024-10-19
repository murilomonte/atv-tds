def main():
    numDigitado = int(input('Insira um número: '))
    cont = 0
    i = 1
    
    while i < (numDigitado + 1):
        divisao = numDigitado % i
        if divisao == 0:
            cont += 1
        i += 1    
    if cont == 2: 
        print('É primo.')
    else:
        print('Não é primo.')
    
if __name__ == "__main__":
    main()