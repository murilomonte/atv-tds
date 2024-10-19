caractere = input('Insira um caractere: ')

def identificador(caractere):
    if caractere.upper() in 'AEIOU':
        print('vogal')
    elif 'B' <= caractere.upper() <= 'Z':
        print('consoante')
    elif caractere in '0123456789':
        print('número')
    else:
        print('símbolo')

identificador(caractere)
