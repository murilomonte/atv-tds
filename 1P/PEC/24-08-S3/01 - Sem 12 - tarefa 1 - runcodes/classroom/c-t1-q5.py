def main():
    quantidade = int(input('Insira a quantidade de dodôs atual: ').strip())

    populacao = quantidade
    ano = 1600
    nascidos = 0
    mortos = 0

    while True:
        if populacao < (quantidade * (10/100)): break
        nascidos = populacao * (1/100)
        mortos = populacao * (6/100)
        populacao = populacao - mortos + nascidos

        print(f'Ano: {round(ano)}. Nascidos: {round(nascidos)}. Mortos: {round(mortos)}. População: {round(populacao)}.')
        ano += 1

        nascidos = 0
        mortos = 0

if __name__ == '__main__':
    main()