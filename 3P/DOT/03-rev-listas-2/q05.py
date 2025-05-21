# 5) Escreva uma função que recebe uma lista com n números inteiros, e retorna uma
# lista com a soma cumulativa dos elementos da lista original onde o i-ésimo
# elemento é a soma dos primeiros i+1 elementos da lista original. Ex: [1,2,3] = [1,3,6]

from random import randint

def calcula_ies(number_list: list[int]) -> list[int]:
    if type(number_list) != list:
        return Exception
    
    if len(number_list) < 2:
        return Exception
    
    for item in number_list:
        if type(item) != int:
            return Exception
        
    final_list: list[int] = []
    sum_buffer: int = 0

    for index in range(1, len(number_list) + 1):
        for item in number_list[:index]:
            sum_buffer += item
        final_list.append(sum_buffer)
        sum_buffer = 0

    return final_list


def random_list(lenght: int, start: int = 0, end: int = 10) -> list[int]:
    """
    Generate random numbers. Default is between 0 and 10.
    """
    number_list: list[int] = []
    for _ in range(lenght):
        number_list.append(randint(start, end))
    return number_list


def main() -> None:
    max_len: int = 3
    random_list_w: list[int] = random_list(lenght=max_len)
    # random_list_w: list[int] = [1, 2, 3]

    print("\n## Lista gerada")
    print("Lista X:", random_list_w)

    print("\n## Resultado")
    print("Res:", calcula_ies(random_list_w))


def tests() -> None:
    print("## Rodando testes")
    print("### calcula_ies")

    lista_a: list[int] = [1,2,3]
    lista_b: list[int] = [1, 2, 3, 4]
    
    assert calcula_ies(lista_a) == [1, 3, 6]
    assert calcula_ies(lista_b) == [1, 3, 6, 10]

    print("- Lista com números inteiros - ok")

    assert calcula_ies("lorem") == Exception
    print("- String qualquer como argumento - ok")

    assert (calcula_ies(5.5)) == Exception
    print("- Número float como argumento - ok")

    assert calcula_ies(True) == Exception
    print("- Booleano como argumento - ok")

    assert calcula_ies([]) == Exception
    print("- List vazia como argumento - ok")

    print("Todos os testes ok")

if __name__ == "__main__":
    tests()
