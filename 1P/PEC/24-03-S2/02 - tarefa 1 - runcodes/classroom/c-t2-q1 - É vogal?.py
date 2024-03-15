def eVogal(caractere):
    return caractere.upper() in 'AEIOU'

caractere = input('Insira o caractere: ')

print('É vogal?: ', eVogal(caractere))

