def calc_nota(n1, n2) -> float:
    media = (n1 + n2) / 2
    return media


def main() -> None:
    while True:
        try:
            n1 = float(input("Insira a primeira nota: "))
            n2 = float(input("Insira a segunda nota: "))
            media = calc_nota(n1, n2)
            print(f"Média semestral: {media}")
            if media >= 6:
                print(f"PARABÉNS! Você foi aprovado.")
            else:
                print(f"Você foi reprovado.")
            break
        except:
            print("Nota inválida. Digite novamente!")


if __name__ == "__main__":
    main()
