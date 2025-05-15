# 6) Dadas duas listas, uma contendo a quantidade e a outra o preço de 20 produtos, elabore um
# programa que calcule e exiba o faturamento que é igual a quantidade x preço. Calcule e exiba
# também o faturamento total que é o somatório de todos os faturamentos, a média dos faturamentos
# e quantos faturamentos estão abaixo da média.
from random import randint


def calc_faturamento_individual(quantidade: list[int], valor: list[int]) -> list[int]:
    if type(quantidade) != list or type(valor) != list:
        return Exception
    if len(quantidade) == 0 or len(valor) == 0:
        return Exception
    faturamento: list[int] = []
    if len(quantidade) == len(valor):
        for index in range(len(quantidade)):
            faturamento.append(quantidade[index] * valor[index])
    else:
        return Exception
    return faturamento


def calc_faturamento_total(faturamento_individual: list[int]) -> int:
    faturamento: int = 0
    for index in range(len(faturamento_individual)):
        faturamento += faturamento_individual[index]
    return faturamento


def random_list(lenght: int, start: int = 0, end: int = 10) -> list[int]:
    """
    Generate random numbers. Default is between 0 and 10.
    """
    number_list: list[int] = []
    for _ in range(lenght):
        number_list.append(randint(start, end))
    return number_list


def main() -> None:
    max_len: int = 20
    quantidade: list[int] = random_list(lenght=max_len, start=1)
    preco: list[int] = random_list(lenght=max_len, start=10, end=100)

    faturamento_individual: list[int] = calc_faturamento_individual(
        quantidade=quantidade, valor=preco
    )
    faturamento_total: int = calc_faturamento_total(
        faturamento_individual=faturamento_individual
    )

    print("\n# Listas iniciais")
    print("Quantidade:", quantidade)
    print("Preço:", preco)
   
    print("\n# Faturamento individual")
    print("Faturamento individual:", faturamento_individual)

    print("\n# Faturamento total")
    print("Faturamento total:", faturamento_total)


def tests() -> None:
    print("## Rodando testes")
    print("### calc_faturamento_individual")

    quantidade: list[int] = [3, 10, 9, 1, 8, 5, 5, 5, 3, 6, 10, 1, 10, 6, 2, 10, 9, 8, 4, 3]
    preco: list[int] = [34, 36, 82, 66, 10, 13, 96, 34, 25, 92, 54, 79, 74, 39, 25, 57, 38, 32, 30, 90]

    assert calc_faturamento_individual(quantidade, preco) == [102, 360, 738, 66, 80, 65, 480, 170, 75, 552, 540, 79, 740, 234, 50, 570, 342, 256, 120, 270]
    print("- Lista com números inteiros - ok")

    assert calc_faturamento_individual([1], [2, 2, 4]) == Exception
    print("- Lista com listas de tamanho diferente - ok")

    assert calc_faturamento_individual(0, 0) == Exception
    print("- 0 como argumento - ok")

    assert calc_faturamento_individual("lorem", 'ipsum') == Exception
    print("- String qualquer como argumento - ok")

    assert (calc_faturamento_individual(5.5, 5.4)) == Exception
    print("- Número float como argumento - ok")

    assert calc_faturamento_individual(True, False) == Exception
    print("- Booleano como argumento - ok")

    assert calc_faturamento_individual([], []) == Exception
    print("- List vazia como argumento - ok")

    print("Todos os testes ok")


if __name__ == "__main__":
    tests()

