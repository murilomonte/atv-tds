# 17) Ler uma lista W de 10 elementos, depois ler um valor V. Contar e escrever quantas vezes o
# valor V ocorre na lista W e escrever também em que posições (índices) da lista W o valor V
# aparece.
# Caso o valor V não ocorra nenhuma vez na lista W, escrever uma mensagem informando isto.


from random import randint


def find_value(value: int, number_list: list[int]) -> list[int]:
    if type(value) != int or type(number_list) != list:
        return Exception
    if len(number_list) == 0:
        return Exception
    index_list: list[int] = []
    for index, item in enumerate(number_list):
        if value == item:
            index_list.append(index)
    return index_list


# Como posso ser quem sou enquanto o mundo é o que é se ao mesmo tempo em que faço parte do mundo, o mundo faz parte mim?

def random_list(lenght: int, start: int = 0, end: int = 10) -> list[int]:
    """
    Generate random numbers. Default is between 0 and 10.
    """
    number_list: list[int] = []
    for _ in range(lenght):
        number_list.append(randint(start, end))
    return number_list


def main() -> None:
    max_len: int = 10
    value: int = 3
    random_list_w: list[int] = random_list(lenght=max_len)

    print("\n## Lista gerada")
    print("Lista X:", random_list_w)

    index_list: list[int] = find_value(value=value, number_list=random_list_w)
    print("\n## Busca")
    print(
        "Quantidade de vezes visto:",
        len(index_list) if len(index_list) > 0 else "Não foi encontrado nenhuma vez.",
    )
    print(
        "Indices onde foi visto:",
        index_list if len(index_list) > 0 else "Não foi encontrado nenhuma vez.",
    )


def tests() -> None:
    print("## Rodando testes")
    print("### find_value")

    lista: list[int] = [2, 8, 9, 2, 3, 1, 7, 0, 3, 6]

    assert find_value(3, lista) == [4, 8]
    print("- Lista com números inteiros - ok")

    assert find_value("lorem", "ipsum") == Exception
    print("- String qualquer como argumento - ok")

    assert (find_value(5.5, 5.5)) == Exception
    print("- Número float como argumento - ok")

    assert find_value(True, False) == Exception
    print("- Booleano como argumento - ok")

    assert find_value([], []) == Exception
    print("- List vazia como argumento - ok")

    print("Todos os testes ok")


if __name__ == "__main__":
    tests()
