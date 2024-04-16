def comparador(n1, n2, n3):
    if n1 != n2 and n2 != n3 and n1 != n3:
        return "Todos os valores são diferentes"
    else:
        return"Todos os valores são iguais" if n1 == n2 and n2 == n3 and n1 == n3 else "Existem dois valores iguais e um diferente" 
    
def main():
    n1 = int(input('Insira o primeiro valor: '))
    n2 = int(input('Insira o segundo valor: '))
    n3 = int(input('Insira o terceiro valor: '))

    print(comparador(n1, n2, n3))

if __name__ == '__main__':
    main()