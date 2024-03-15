def eLetra(caractere):
    return 'A' <= caractere.upper() <= 'Z'

def eNum(caractere):
    return caractere in '0123456789'

def comparacao(caractere):
    return not eLetra(caractere) and not eNum(caractere)

caractere = input().strip()
print(comparacao(caractere))