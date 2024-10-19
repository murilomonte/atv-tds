def eLetra(caractere):
    return 'A' <= caractere.upper() <= 'Z'

def eNum(caractere):
    return caractere <= '9' or caractere in '0123456789'

def comparacao(caractere):
    return not eLetra(caractere) and not eNum(caractere)

caractere = input('Insira o caractere: ')
print('É símbolo?: ', comparacao(caractere))