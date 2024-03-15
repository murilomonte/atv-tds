def eLetra(caractere):
    return 'A' <= caractere.upper() <= 'Z'

caractere = input('Insira o caractere: ')
print('É letra?: ', eLetra(caractere))
