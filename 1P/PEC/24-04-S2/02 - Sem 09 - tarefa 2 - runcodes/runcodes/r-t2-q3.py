# Escreva um programa que leia uma data no formado DDMMAAA e informe se é uma data válida.
# OBS: Use apenas condicionais e os tipos básicos do Python; Não utilize bibliotecas do Python que tratam datas;
# Considere que em anos bissextos o mês de fevereiro tem 29 dias.

def data_funcao(data):
    ano = data % 10000
    data = data // 10000
    mes = data % 100
    data = data // 100
    dia = data 

    if (1000 <= ano <= 9999):
        if (ano % 4 == 0) and (mes == 2) and (ano % 100 != 0) or (ano % 400 == 0):
                return True if (0 < dia <= 29) else False
                
        else:
            if mes == 2:
                return True if (0 < dia <= 28) else False
            elif mes in [1, 3, 5, 7, 8, 10, 12]:
                return True if (0 < dia <= 31) else False
            elif mes in [4, 6, 9, 11]:
                return True if (0 < dia <= 30) else False
            else:
                return False
    else:
        return False
    
def main():
    data = int(input())
    print(f'{data_funcao(data)}')

if __name__ == '__main__':
    main()
