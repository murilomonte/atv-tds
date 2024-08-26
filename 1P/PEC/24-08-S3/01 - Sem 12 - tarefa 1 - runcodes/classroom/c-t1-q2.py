def main():
    carro = float(input('Qual o valor do carro?: ').strip())

    mes = 0
    poupanca = 10000
    
    while True:
        if poupanca >= carro: break
        mes += 1
        poupanca += poupanca * (0.7/100)
        carro += carro * (0.4/100)
    
    print('Irá demorar', mes, 'meses para a polpança ultrapassar o valor do carro.')

if __name__ == '__main__':
    main()