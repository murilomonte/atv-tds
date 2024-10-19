def calcular(ano_atual, ano_nasc):
    return ano_atual - ano_nasc

   
def main():
    dia_atual = int(input('Dia atual: '))
    mes_atual = int(input('Mês atual: '))
    ano_atual = int(input('Ano atual: '))
    
    dia_nasc = int(input('Dia atual: '))
    mes_nasc = int(input('Mes atual: '))
    ano_nasc = int(input('Ano atual: '))

    idade = calcular(ano_atual, ano_nasc)
    
    if mes_atual< mes_nasc  or dia_atual < dia_nasc:
        print(idade - 1) 
    else:
        print(idade)

if __name__ == '__main__':
    main()