nome = str(input('').strip())
sexo = str(input('').strip())

def sexIdent(sexo):
    if sexo == '1':
        return 'Ilmo Sr.'
    elif sexo == '2':
        return 'Ilma Sra.'
    else:
        return 'Sexo inválido'

print(sexIdent(sexo), nome)