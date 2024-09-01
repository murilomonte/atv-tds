def esta_ordenado(lista):
    ordenados = 0
    indice = 1
    for valor in lista:
        if indice == len(lista): break
        if valor <= lista[indice]:
            ordenados += 1
        indice += 1
    if ordenados + 1 == len(lista):
        return True
    else:
        return False

def main():
    lista = []
    qt = int(input().strip())

    while len(lista) < qt:
        val = input().strip()
        if 'A' <= val.upper() < 'Z':
            lista.append(ord(val))
        else:
            lista.append(float(val))
    
    if esta_ordenado(lista):
        print('LISTA ORDENADA')
    else:
        print('LISTA NÃO ORDENADA')

if __name__ == '__main__':
    main()
