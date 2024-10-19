nome = str(input('Qual o seu nome? '))
sexo = str(input('Qual o seu sexo? (1 - masc.; 2 - fem.): '))

def sexIdent(sexo):
    if sexo == '1':
        return 'Ilmo Sr.'
    elif sexo == '2':
        return 'Ilma Sra.'
    else:
        return 'Sexo inválido'

print(sexIdent(sexo), nome)