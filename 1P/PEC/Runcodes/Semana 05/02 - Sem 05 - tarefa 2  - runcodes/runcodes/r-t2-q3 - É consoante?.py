def eVogal(caractere):
    return caractere.upper() in 'AEIOU'

def eLetra(caractere):
    return 'A' <= caractere.upper() <= 'Z'

def eCons(caractere):
    return eLetra(caractere) and not eVogal(caractere)

caractere = input().strip()
print(eCons(caractere))