# 9. Escreva uma função que recebe 2 números inteiros n1 e n2 como entrada e retorna a soma de todos os números inteiros contidos
# no intervalo [n1,n2]. Use esta função em um programa que lê n1 e n2 do usuário e imprime a soma.

def get_soma(n1: int, n2: int) -> int:
    if type(n1) != int or type(n2) != int:
        return Exception
    soma: int = 0
    for i in range(n1, n2 + 1):
        if i == n1:
            soma = i
        else:
            soma += i
    return soma



def tests() -> None:
    print("## Rodando testes")
    print("### get_soma")

    assert get_soma(1, 10) == 55
    assert get_soma(20, 45) == 845
    print("- Interválos entre números inteitor - ok")

    assert get_soma("sim", "não") == Exception
    print("- String qualquer como argumento - ok")

    assert (get_soma(5.5, 5.5)) == Exception
    print("- Número float como argumento - ok")

    assert get_soma(True, False) == Exception
    print("- Booleano como argumento - ok")

    assert get_soma([], []) == Exception
    print("- List como argumento - ok")

    print("Todos os testes ok")


if __name__ == "__main__":
    tests()
