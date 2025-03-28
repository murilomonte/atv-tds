# 10. Escreva um programa composto de uma função Max e o programa principal como segue:
# a) A função Max recebe como parâmetros de entrada dois números inteiros e retorna o maior. Se forem iguais retorna qualquer um
# deles;
# b) O programa principal lê 4 séries de 4 números a, b. Para cada série lida imprime o maior dos quatro números usando a função
# Max.


def max(n1: int, n2: int, n3: int, n4: int) -> int:
    if n1 == n2 == n3 == n4:
        return n1
    lista: list[int] = [n1, n2, n3, n4]
    maior: int = lista[0]
    for i in lista:
        if i > maior:
            maior = i
    return maior


def main() -> None:
    lista_series: list[int] = []
    i: int = 0
    while i < 4:
        i+= 1
        try:
            n1: int = int(input("Digite o primeiro número: "))
            n2: int = int(input("Digite o segundo número: "))
            n3: int = int(input("Digite o terceiro número: "))
            n4: int = int(input("Digite o quarto número: "))
            
            maior: int = max(n1, n2, n3, n4)
            print(f"O maior entre {n1}, {n2}, {n3} e {n4} é: {maior}")
            lista_series.append(maior)
        except ValueError:
            i -= 1
            print("\nEntrada inválida. Digite apenas números!")

if __name__ == "__main__":
    main()
