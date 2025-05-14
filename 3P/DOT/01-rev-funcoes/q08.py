# 8. Escreva uma função que lê um caractere digitado pelo usuário e retorna este caractere somente se ele for igual a 'S' ou 'N'. Se o
# caractere não for nem 'S' nem 'N', a função imprime a mensagem 'Caractere inválido. Digite novamente'. Use esta função em um
# programa que fica lendo do usuário um número qualquer e imprime este número ao cubo na tela. O programa deve ficar lendo os
# números até o usuário responder 'N' à pergunta se ele deseja continuar ou não.


def get_comando(entrada: str) -> str:
    if type(entrada) != str:
        return Exception
    # comando: str = str(input("Deseja continuar? (S ou N): "))
    comando: str = entrada
    if comando.upper() == "N":
        print("Saindo...")
        return "N"
    elif comando.upper() == "S":
        return "S"
    else:
        return "Entrada inválida."


def tests() -> None:
    print("## Rodando testes")
    print("### get_comando")

    assert get_comando("s") == "S"
    assert get_comando("N") == "N"
    print("- 'N' ou 'S' (mínusculo e maiúsculo) como argumento - ok")

    assert get_comando("sim") == "Entrada inválida."
    print("- String qualquer como argumento - ok")

    assert get_comando(1) == Exception
    print("- Número int como argumento - ok")

    assert (get_comando(5.5)) == Exception
    print("- Número float como argumento - ok")

    assert get_comando(True) == Exception
    print("- Booleano como argumento - ok")

    assert get_comando([]) == Exception
    print("- List como argumento - ok")

    print("Todos os testes ok")


if __name__ == "__main__":
    tests()
