# 4) Escreva uma função que recebe uma lista com n números inteiros, e determina a
# maior soma de qualquer seguimento da lista. Ex: [5, -2, -2, -7, 3, 15, 10, -3, 9, -6, 4, 1] = 34

from random import randint

def algoritmo_linear(lista: list[int]) -> int:
    max_soma_interna = lista[0]
    max_soma_global = lista[0]

    ## Para cada número da lista, testa se o mesmo é maior que a soma do anterior com ele mesmo
    for num in lista[1:]:
        max_soma_interna = max(num, max_soma_interna + num) # Escolhe se deve continuar somando ou deve substituir o valor
        max_soma_global = max(max_soma_global, max_soma_interna) # Se a soma da sublista for maior, troca o valor global
    
    return max_soma_global


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
    random_list_w: list[int] = random_list(lenght=max_len)

    print("\n## Lista gerada")
    print("Lista X:", random_list_w)

    largest_sum: int = algoritmo_linear(lista=random_list_w)
    print("\n# Maior soma")
    print(f"Valor: {largest_sum}")

def testes() -> None:
    assert algoritmo_linear([5, -2, -2, -7, 3, 15, 10, -3, 9, -6, 4, 1]) == 34
    print('Teste ok')

test_mode = True

if __name__ == "__main__":
    if test_mode:
        testes()
    else:
        main()
