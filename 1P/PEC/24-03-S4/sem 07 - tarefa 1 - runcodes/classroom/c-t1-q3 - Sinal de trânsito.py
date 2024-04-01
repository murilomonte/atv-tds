sinal = str(input('Qual é a cor do sinal?: '))

def semaforo(sinal):
    if sinal.upper() == 'V':
        print('Siga')
    elif sinal.upper() == 'A':
        print('Atenção')
    elif sinal.upper() == 'E':
        print('Pare')
    else:
        print('Insira um valor válido')

semaforo(sinal)