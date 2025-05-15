# 18) Ler uma lista X de 10 elementos. A seguir copiar todos os valores negativos da lista X para
# uma lista R, sem deixar elementos vazios entre os valores copiados. Escrever as listas X e R.

from random import randint

def transfer_list(number_list: list[int]) -> list[int]:
    if type(number_list) != list:
        return Exception
    if len(number_list) == 0:
        return Exception
    list_r: list[int] = []
    for item in number_list:
        if item < 0:
            list_r.append(item)
    return list_r


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
    random_list_w: list[int] = random_list(lenght=max_len, start=-10, end=10)

    print("\n## Lista gerada")
    print("Lista X:", random_list_w)

    copy_list: list[int] = transfer_list(number_list=random_list_w)
    print("\n ## Lista copiada")
    print("Lista R:", copy_list)


def tests() -> None:
    print("## Rodando testes")
    print("### transfer_list")

    lista: list[int] = [1, -4, -1, -6, -8, 8, 7, -10, -9, -10]

    assert transfer_list(lista) == [-4, -1, -6, -8, -10, -9, -10]
    print("- Lista com números inteiros - ok")

    assert transfer_list("lorem") == Exception
    print("- String qualquer como argumento - ok")

    assert (transfer_list(5.5)) == Exception
    print("- Número float como argumento - ok")

    assert transfer_list(True) == Exception
    print("- Booleano como argumento - ok")

    assert transfer_list([]) == Exception
    print("- List vazia como argumento - ok")

    print("Todos os testes ok")


if __name__ == "__main__":
    tests()
