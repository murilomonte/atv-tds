def eLetra(caractere):
    return 'A' <= caractere.upper() <= 'Z'

def eNum(caractere):
    return caractere in '0123456789'

def comparacao(caractere):
    return eLetra(caractere) or eNum(caractere)

caractere = input().strip()
print(comparacao(caractere))