# 6) Dadas duas listas, uma contendo a quantidade e a outra o preço de 20 produtos, elabore um
# programa que calcule e exiba o faturamento que é igual a quantidade x preço. Calcule e exiba
# também o faturamento total que é o somatório de todos os faturamentos, a média dos faturamentos
# e quantos faturamentos estão abaixo da média.
from random import randint


def calc_faturamento_individual(quantidade: list[int], valor: list[int]) -> list[int]:
    faturamento: list[int] = []
    if len(quantidade) == len(valor):
        for index in range(len(quantidade)):
            faturamento.append(quantidade[index] * valor[index])
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


if __name__ == "__main__":
    main()
