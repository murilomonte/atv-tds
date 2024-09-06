def filtro(lista):
    unicos = []
    for numero in lista:
        if numero not in unicos: unicos.append(numero)
    return unicos

def main():
    lista = []

    while len(lista) < 20:
        num = int(input().strip())
        lista.append(num)
    
    print(filtro(lista))

if __name__ == '__main__':
    main()