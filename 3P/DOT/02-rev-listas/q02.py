# 2) Faça um programa que grave uma lista com dez números reais, calcule e mostre a quantidade
# de números negativos e a soma dos números positivos dessa lista.

from random import randint


def calc(number_list: list[int]) -> dict[str, int]:
    if type(number_list) != list:
        return Exception
    if len(number_list) == 0:
        return Exception
    qnt_negative: int = 0
    sum_positive: int = 0
    for num in number_list:
        if num < 0:
            qnt_negative += 1
        else:
            sum_positive += num
    return {"negativos": qnt_negative, "soma_pos": sum_positive}


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
    random_number_list: list[int] = random_list(lenght=max_len, end=10, start=-10)

    print("\n## Todos os números")
    print("Lista:", random_number_list)
    print("Tamanho:", len(random_number_list))

    calculo: dict[str, int] = calc(random_number_list)

    print("\n## Todos os números")
    print("Quantidade de negativos:", calculo["negativos"])
    print("Soma de todos os positivos:", calculo["soma_pos"])


def tests() -> None:
    print("## Rodando testes")
    print("### calc")

    lista: list[int] = [6, 8, -10, 9, 6, -3, 5, 2, 6, 7]

    assert calc(lista) == {"negativos": 2, "soma_pos": 49}
    print("- Lista com números inteiros - ok")

    assert calc(0) == Exception
    print("- 0 como argumento - ok")

    assert calc("lorem") == Exception
    print("- String qualquer como argumento - ok")

    assert (calc(5.5)) == Exception
    print("- Número float como argumento - ok")

    assert calc(True) == Exception
    print("- Booleano como argumento - ok")

    assert calc([]) == Exception
    print("- List vazia como argumento - ok")

    print("Todos os testes ok")


if __name__ == "__main__":
    tests()
