# 8) Dada uma lista contendo letras do alfabeto, elabore um programa para verificar quantas vezes
# ocorreu a letra ‘A’.
# OBS: Fazer crítica na entrada do caractere para aceitar somente letras.


def find(item: str, list: list[str]) -> int:
    times_found: int = 0
    for i in list:
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



if __name__ == "__main__":
    main()
