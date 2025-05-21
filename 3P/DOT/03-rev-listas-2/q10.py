# 10)Escreva uma função que recebe uma lista com n números inteiros, e determina a
# maior soma dos números que se repetem da lista. Ex: [5, -2, -2, 5, 3, 5, 10, -2, 3, 10, 3, 1] = 20

from random import randint

# Para cada número, percorre novamente a lista. Se o mesmo for igual ao número principal, soma e guarda em uma variável chamada maior_soma_interna. Caso a mesma seja maior que outra variável chamada maior_soma_global, substitua.

def calc_seq(number_list: list[int]) -> int:
    if type(number_list) != list:
        return Exception
    
    if len(number_list) < 2:
        return Exception
    
    for item in number_list:
        if type(item) != int:
            return Exception

    global_sum: int = 0
    internal_sum: int = 0
    ocurrences: int = 0 ## Remover caso seja preciso considerar também números que não se repetem
    for number in number_list:
        internal_sum = 0
        ocurrences = 0
        for internal_number in number_list:
            if number == internal_number:
                internal_sum += internal_number
                ocurrences += 1
            if internal_sum > global_sum and ocurrences > 1: 
                global_sum = internal_sum
    return global_sum



def random_list(lenght: int, start: int = 0, end: int = 10) -> list[int]:
    """
    Generate random numbers. Default is between 0 and 10.
    """
    number_list: list[int] = []
    for _ in range(lenght):
        number_list.append(randint(start, end))
    return number_list


def main() -> None:
    max_len: int = 4
    random_list_w: list[int] = random_list(lenght=max_len)
    # random_list_w: list[int] = [5, -2, -2, 5, 3, 5, 10, -2, 3, 10, 3, 1]

    print("\n## Lista gerada")
    print("Lista X:", random_list_w)

    print("\n## Resultado final")
    print("Res:", calc_seq(random_list_w))


def tests() -> None:
    print("## Rodando testes")
    print("### calc_seq")

    lista_a: list[int] = [5, -2, -2, 5, 3, 5, 10, -2, 3, 10, 3, 1]

    assert calc_seq(lista_a) == 20

    print("- Lista com números inteiros - ok")

    assert calc_seq("lorem") == Exception
    print("- String qualquer como argumento - ok")

    assert (calc_seq(5.5)) == Exception
    print("- Número float como argumento - ok")

    assert calc_seq(True) == Exception
    print("- Booleano como argumento - ok")

    assert calc_seq([]) == Exception
    print("- List vazia como argumento - ok")

    print("Todos os testes ok")

if __name__ == "__main__":
    tests()
