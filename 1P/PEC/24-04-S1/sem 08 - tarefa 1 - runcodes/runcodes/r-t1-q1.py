def calcular(ano_atual, ano_nasc):
    return ano_atual - ano_nasc

   
def main():
    dia_atual = int(input())
    mes_atual = int(input())
    ano_atual = int(input())
    
    dia_nasc = int(input())
    mes_nasc = int(input())
    ano_nasc = int(input())

    idade = calcular(ano_atual, ano_nasc)
    
    if mes_atual< mes_nasc  or dia_atual < dia_nasc:
        print(idade - 1) 
    else:
        print(idade)

if __name__ == '__main__':
    main()

    