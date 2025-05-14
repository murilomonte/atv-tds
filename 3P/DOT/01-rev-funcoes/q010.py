# 10. Escreva um programa composto de uma função Max e o programa principal como segue:
# a) A função Max recebe como parâmetros de entrada dois números inteiros e retorna o maior. Se forem iguais retorna qualquer um
# deles;
# b) O programa principal lê 4 séries de 4 números a, b. Para cada série lida imprime o maior dos quatro números usando a função
# Max.


def max(n1: int, n2: int, n3: int, n4: int) -> int:
    if (type(n1) != int) or (type(n2) != int) or (type(n3) != int) or (type(n4) != int):
        return Exception
    if n1 == n2 == n3 == n4:
        return n1
    lista: list[int] = [n1, n2, n3, n4]
    maior: int = lista[0]
    for i in lista:
        if i > maior:
            maior = i
    return maior


def tests() -> None:
    print("## Rodando testes")
    print("### max")

    assert max(1, 10, 34, -3) == 34
    assert (
        max(
            20,
            45,
            -45,
            1234,
        )
        == 1234
    )
    print("- Números inteiros - ok")

    assert max("lorem", "ipsum", "dolor", "sit") == Exception
    print("- String qualquer como argumento - ok")

    assert (max(5.5, 5.5, 3.4, 5.6)) == Exception
    print("- Número float como argumento - ok")

    assert max(True, False, False, True) == Exception
    print("- Booleano como argumento - ok")

    assert max([], [], [], []) == Exception
    print("- List como argumento - ok")

    print("Todos os testes ok")


if __name__ == "__main__":
    tests()
