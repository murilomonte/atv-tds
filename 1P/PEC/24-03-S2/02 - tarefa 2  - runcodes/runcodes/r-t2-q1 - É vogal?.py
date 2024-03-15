def eVogal(caractere):
    return caractere.upper() in 'AEIOU'

caractere = input().strip()

print(eVogal(caractere))

