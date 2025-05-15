# 8) Dada uma lista contendo letras do alfabeto, elabore um programa para verificar quantas vezes
# ocorreu a letra ‘A’.
# OBS: Fazer crítica na entrada do caractere para aceitar somente letras.


def find(item: str, lista: list[str]) -> int:
    if type(item) != int or type(lista) != list:
        return Exception
    times_found: int = 0
    for i in lista:
        if item == i:
            times_found += 1
    return times_found

def main() -> None:
    letter_list: list[str] = []

    while len(letter_list) <= 10:
        try:
            letter: str = str(input("Insira uma letra: "))

            if "A" <= letter <= "z":
                letter_list.append(letter)
            else:
                raise ValueError
        except ValueError:
            print("Somente letras são aceitas (a-z/A-Z)")

    print('\n## Análise')
    print('Lista gerada:', letter_list)
    print(f'Vezes em que a letra "A" foi vista:', find(item='A', list=letter_list))


def tests() -> None:
    print("## Rodando testes")
    print("### find")

    lista: list[int] = [6, 8, -10, 9, 6, -3, 5, 2, 6, 7]

    assert find(item=7, lista=lista) == 1
    assert find(item=1, lista=lista) == 0
    print("- Lista com números inteiros - ok")

    assert find("lorem", "ipsum") == Exception
    print("- String qualquer como argumento - ok")

    assert (find(5.5, 5.4)) == Exception
    print("- Número float como argumento - ok")

    assert find(True, False) == Exception
    print("- Booleano como argumento - ok")

    assert find([], []) == Exception
    print("- List vazia como argumento - ok")

    print("Todos os testes ok")


if __name__ == "__main__":
    tests()