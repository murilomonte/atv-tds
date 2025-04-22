# 12) Deseja-se publicar o número de acertos de cada aluno em uma prova em forma de testes. A
# prova consta de 30 questões, cada uma com cinco alternativas identificadas por A, B, C, D e E.
# Para isso são dados:
# o cartão gabarito;
# o número de alunos da turma;
# o cartão de respostas para cada aluno, contendo o seu número e suas respostas.


from random import choices


def checkAnswer(key: list[str], answers: list[str]) -> int:
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

    num_questions: int = 30
    num_students: int = 20

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
        print(f'\n## Estudante n° {student}')
        print(f'Respostas: {test_answers}')
        print(f'Pontuação: {points}')


if __name__ == "__main__":
    main()
