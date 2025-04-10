# 2) Faça um programa que grave uma lista com dez números reais, calcule e mostre a quantidade
# de números negativos e a soma dos números positivos dessa lista.

from random import randint


def calc(number_list: list[int]) -> dict[str, int]:
    qnt_negative: int = 0
    sum_positive: int = 0
    for num in number_list:
        if num < 0:
            qnt_negative += 1
        else:
            sum_positive += num
    return {"negativos": qnt_negative, "soma_pos": sum_positive}


def random_list(lenght: int, max_num: int, min_num: int = 0) -> list[int]:
    number_list: list[int] = []
    for _ in range(lenght):
        number_list.append(randint(min_num, max_num))
    return number_list


def main() -> None:
    max_len: int = 20
    random_number_list: list[int] = random_list(lenght=max_len, max_num=10, min_num=-10)

    print("\n## Todos os números")
    print("Lista:", random_number_list)
    print("Tamanho:", len(random_number_list))

    calculo: dict[str, int] = calc(random_number_list)

    print("\n## Todos os números")
    print("Quantidade de negativos:", calculo["negativos"])
    print("Soma de todos os positivos:", calculo["soma_pos"])


if __name__ == "__main__":
    main()
