def contador(lista, num):
    contador = 0
    for dado in lista:
        if dado == num: contador += 1
    return contador

def main():
    lista = []
    print('Insira qualquer número para atribuir a lista. (Use 0 quando quiser parar.)')
    while True:
        num = int(input('> ').strip())
        if num == 0: break
        lista.append(num)
    numero = int(input('Insira um número para saber sua recorrencia na lista: ').strip())

    print('Lista completa:', lista)
    print('Número requisitado:', numero)
    print('Ocorrência:', contador(lista, numero))

if __name__ == '__main__':
    main()