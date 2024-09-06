def comprimento(lista):
    contador = 0
    for dado in lista:
        contador += 1
    return contador

def inverter(lista):
    listaInv = []
    for dado in lista:
        listaInv.insert(0, dado)
    return listaInv

def minimo(lista):
    menor = lista[0]
    for dado in lista:
        if dado < menor: menor = dado
    return menor

def maximo(lista):
    maior = lista[0]
    for dado in lista:
        if dado > maior: maior = dado
    return maior

def soma(lista):
    resultado = 0
    for dado in lista:
        resultado += dado
    return resultado

def main():
    lista = []
    while True:
        num = int(input().strip())
        if num == 0: break
        lista.append(num)

    print(lista)
    print(comprimento(lista))
    print(inverter(lista))
    print(minimo(lista))
    print(maximo(lista))
    print(soma(lista))

if __name__ == '__main__':
    main()