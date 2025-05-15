# 12) Deseja-se publicar o número de acertos de cada aluno em uma prova em forma de testes. A
# prova consta de 30 questões, cada uma com cinco alternativas identificadas por A, B, C, D e E.
# Para isso são dados:
# o cartão gabarito;
# o número de alunos da turma;
# o cartão de respostas para cada aluno, contendo o seu número e suas respostas.


from random import choices


def checkAnswer(key: list[str], answers: list[str]) -> int:
    if (type(key) != list) or (type(answers) != list):
        return Exception
    if (len(key) == 0) or (len(answers) == 0):
        return Exception
    if len(key) != len(answers):
        raise ValueError("As listas não têm a mesma quantide de itens.")

    points: int = 0
    for number, question in enumerate(key):
        if question == answers[number]:
            points += 1
    return points


def random_letters_list(length: int, letters: list[str]) -> list[str]:
    """
    Generate random letters
    """
    letter_list = choices(letters, k=length)
    return letter_list


def main() -> None:
    alternatives: list[str] = ["A", "B", "C", "D", "E"]

    num_questions: int = 5
    num_students: int = 2

    answer_key: list[str] = random_letters_list(
        length=num_questions,
        letters=alternatives,
    )
    print("## Gabarito")
    print(f"Lista: {answer_key}")

    for student in range(num_students):
        test_answers: list[str] = random_letters_list(
            length=num_questions,
            letters=alternatives,
        )
        points = checkAnswer(key=answer_key, answers=test_answers)
        print(f"\n## Estudante n° {student}")
        print(f"Respostas: {test_answers}")
        print(f"Pontuação: {points}")


def tests() -> None:
    print("## Rodando testes")
    print("### checkAnswer")

    gabarito: list[int] = ['A', 'A', 'A', 'D', 'D']
    respostas: list[int] = ['D', 'C', 'A', 'A', 'C']

    assert checkAnswer(key=gabarito, answers=respostas) == 1
    print("- Gabarito e respostas corretos - ok")

    assert checkAnswer(0, 0) == Exception
    print("- 0 como argumento - ok")

    assert checkAnswer("lorem", "ipsum") == Exception
    print("- String qualquer como argumento - ok")

    assert (checkAnswer(5.5, 5.5)) == Exception
    print("- Número float como argumento - ok")

    assert checkAnswer(True, False) == Exception
    print("- Booleano como argumento - ok")

    assert checkAnswer([], []) == Exception
    print("- List vazia como argumento - ok")

    print("Todos os testes ok")


if __name__ == "__main__":
    tests()
