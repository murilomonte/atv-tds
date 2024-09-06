def contador(lista, num):
    contador = 0
    for dado in lista:
        if dado == num: contador += 1
    return contador

def main():
    lista = []
    while True:
        num = int(input().strip())
        if num == 0: break
        lista.append(num)
    numero = int(input().strip())

    print(lista)
    print(numero)
    print(contador(lista, numero))

if __name__ == '__main__':
    main()