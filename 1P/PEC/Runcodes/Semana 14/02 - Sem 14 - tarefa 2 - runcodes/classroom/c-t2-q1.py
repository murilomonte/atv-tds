def maior(lista):
    maior = lista[0]
    posi = 0
    indice = 0
    for dado in lista:
        if dado > maior: 
            maior = dado
            posi = indice
        indice += 1
    return maior, posi

def main():
    lista = []
    print('Insira 10 números:')
    while len(lista) < 10:
        num = int(input('> ').strip())
        lista.append(num)
    print('Lista completa:', lista)
    print('Maior número:', maior(lista)[0])
    print('Posição:', maior(lista)[1])
    

if __name__ == '__main__':
    main()