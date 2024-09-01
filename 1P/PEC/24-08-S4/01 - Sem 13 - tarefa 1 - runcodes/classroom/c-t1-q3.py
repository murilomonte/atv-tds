def main():
    lista = []
    num = int(input().strip())

    # a - preencha com valores reais lidos pelo teclado e imprima na ordem inversa. Considere até 4 (quatro) casas decimais.
    lista = []
    while len(lista) < num:
        valor = float(input().strip())
        lista.insert(0, float(f'{valor:.4f}'))
    print(lista)

    # b - preencha com n notas lidas pelo teclado e imprima as notas e a média na tela. Considere 1 (uma) casa decimal. Se n = 0, imprima “SEM NOTAS”.
    lista = []
    while len(lista) < num:
        nota = float(input().strip())
        if nota == 0: break
        lista.append(nota)
    print(lista)
    if len(lista) == 0:
        print("SEM NOTAS")
    else:
        print(f'{(sum(lista)) / len(lista):.1f}')

    # c - preencha com n letras lidas pelo teclado e imprima quantas vogais foram lidas. Imprima as consoantes. Dica: certifique-se de ler apenas um caractere com input()[0]
    lista = []
    while len(lista) < num:
        letra = str(input()[0].strip())
        lista.append(letra)
    
    qtVogais = 0
    consoantes = []
    for dado in lista:
        if dado.upper() in 'AEIOU':
            qtVogais += 1
        if dado.upper() not in 'AEIOU' and 'B' <= dado.upper() <= 'Z':
            consoantes.append(dado)
    print(qtVogais)
    print(consoantes)

if __name__ == '__main__':
    main()