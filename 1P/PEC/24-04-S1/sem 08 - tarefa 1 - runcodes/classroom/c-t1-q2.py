def main():
    dia_1 = int(input('Dia 1: '))
    mes_1 = int(input('Mês 1: '))
    ano_1 = int(input('Ano 1: '))

    dia_2 = int(input('Dia 2: '))
    mes_2 = int(input('Mês 2: '))
    ano_2 = int(input('Ano 2: '))

    if ano_1 > ano_2 :
        print(f'{dia_1}/{mes_1}/{ano_1}')
    # 02/04/2024 - 02/04/2024 
    elif ano_1 == ano_2 and mes_1 >= mes_2 and dia_1 >= dia_2:
        print(f'{dia_1}/{mes_1}/{ano_1}')
    else:
        print(f'{dia_2}/{mes_2}/{ano_2}')

if __name__ == '__main__':
    main()