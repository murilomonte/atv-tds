# 13) Tentando descobrir se um dado era viciado, um dono de cassino honesto (ha! ha! ha! ha!) o
# lançou n vezes. Dados os n resultados dos lançamentos, determinar o número de ocorrências de
# cada face.


from random import choice


def roll_dice() -> int:
    possible_faces: list[int] = [1, 2, 3, 4, 5, 6]
    face: int = choice(seq=possible_faces)
    return face


def check_dice(times_rolled: int) -> dict[int, int]:
    if type(times_rolled) != int:
        return Exception
    if times_rolled <= 0:
        return Exception
    
    dice_faces: dict[int, int] = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
    }

    for _ in range(times_rolled):
        chosen_face: int = roll_dice()
        for key in dice_faces:
            if chosen_face == key:
                dice_faces[key] += 1

    return dice_faces


def main() -> None:
    times_rolled: int = 10
    chosen_faces: dict[int, int] = check_dice(times_rolled=times_rolled)
    print("# Checagem")
    print(f"Vezes jogadas: {times_rolled}")

    print("\n## Resultados")
    for key in chosen_faces:
        print(f"{key} caiu {chosen_faces[key]} vez(es).")



def tests() -> None:
    print("## Rodando testes")
    print("### check_dice")

    assert check_dice(0) == Exception
    print("- 0 como argumento - ok")

    assert check_dice("lorem") == Exception
    print("- String qualquer como argumento - ok")

    assert (check_dice(5.5)) == Exception
    print("- Número float como argumento - ok")

    assert check_dice(True) == Exception
    print("- Booleano como argumento - ok")

    assert check_dice([]) == Exception
    print("- List vazia como argumento - ok")

    print("Todos os testes ok")


if __name__ == "__main__":
    tests()

