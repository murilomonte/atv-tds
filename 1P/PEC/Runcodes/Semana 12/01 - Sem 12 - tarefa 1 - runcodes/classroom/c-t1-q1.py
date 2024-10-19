def main():
    distancia = int(input('Insira a distancia: ').strip())

    minuto = 0
    tortuga = distancia
    lebre = 0
    
    while True:
        if lebre >= tortuga: break
        tortuga += 1
        lebre += 10
        minuto += 1
    
    print('Demorará', minuto, 'minutos para a lebre ultrapassar a tartaruga.')

if __name__ == '__main__':
    main()