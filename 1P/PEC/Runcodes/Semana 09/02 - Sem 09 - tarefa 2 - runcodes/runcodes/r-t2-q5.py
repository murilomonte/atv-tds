# Faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

# a) "Telefonou para a vítima ?"

# b) "Esteve no local do crime ?"

# c) "Mora perto da vítima ?"

# d) "Devia para a vítima ?"

# e) "Já trabalhou com a vítima ?"

# Considere “S” para sim ou “N” para não. O programa deve emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeito", entre 3 ou 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

def classificacao(contagem):
    if contagem == 0 or contagem == 1:
        return 'Inocente'
    elif contagem == 2:
        return 'Suspeito'
    elif contagem == 3 or contagem == 4:
        return 'Cúmplice'
    elif contagem == 5:
        return 'Assassino'

def main():
    a = input().upper().strip()
    b = input().upper().strip()
    c = input().upper().strip()
    d = input().upper().strip()
    e = input().upper().strip()
    
    contador = 0
    contador = contador + 1 if a == 'S' else contador + 0
    contador = contador + 1 if b == 'S' else contador + 0
    contador = contador + 1 if c == 'S' else contador + 0
    contador = contador + 1 if d == 'S' else contador + 0
    contador = contador + 1 if e == 'S' else contador + 0

    print(classificacao(contador))

if __name__ == '__main__':
    main()
