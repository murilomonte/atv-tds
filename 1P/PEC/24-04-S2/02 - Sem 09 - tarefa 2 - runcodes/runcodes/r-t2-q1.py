# Escreva um programa que leia um número e exiba o dia correspondente da semana. (1-domingo, 2-segunda-feira, 3-terça-feira etc.), se digitar outro valor deve aparecer “valor inválido”.

def diaSem(dia):
    if dia == 1:
        return 'domingo'
    elif dia == 2:
        return 'segunda-feira'
    elif dia == 3:
        return 'terça-feira'
    elif dia == 4:
        return 'quarta-feira'
    elif dia == 5:
        return 'quinta-feira'
    elif dia == 6:
        return 'sexta-feira'
    elif dia == 7:
        return 'sábado'
    else:
        return 'valor inválido'

def main():
    dia = int(input())

    print(diaSem(dia))

if __name__ == '__main__':
    main()
