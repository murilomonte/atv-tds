def eLetra(caractere):
    return 'A' <= caractere.upper() <= 'Z'

caractere = input().strip()
print(eLetra(caractere))
