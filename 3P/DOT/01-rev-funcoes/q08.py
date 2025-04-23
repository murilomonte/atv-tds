# 8. Escreva uma função que lê um caractere digitado pelo usuário e retorna este caractere somente se ele for igual a 'S' ou 'N'. Se o
# caractere não for nem 'S' nem 'N', a função imprime a mensagem 'Caractere inválido. Digite novamente'. Use esta função em um
# programa que fica lendo do usuário um número qualquer e imprime este número ao cubo na tela. O programa deve ficar lendo os
# números até o usuário responder 'N' à pergunta se ele deseja continuar ou não.
def get_comando() -> str:
    comando: str = str(input("Deseja continuar? (S ou N): "))
    if comando.upper() == "N":
        print("Saindo...")
        return 'N'
    elif comando.upper() == "S":
        return 'S'
    else:
        print("Entrada inválida.")
        get_comando()

def main():
    while True:
        try:
            num: int = int(input("Insira um número: "))
            print(f"{num}^2 -> {num ** 2}")

            comando: str = get_comando()
            if comando == 'N':
                break
        except ValueError:
            print("Entrada inválida. Insira um número.")


if __name__ == "__main__":
    main()
