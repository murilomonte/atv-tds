# 5. Faça um programa que leia a altura e o sexo (codificado da seguinte forma: 1:feminino 2:masculino) de uma pessoa. Depois faça uma função chamada peso ideal que receba a altura e o sexo via parâmetro e que calcule e retorne seu peso ideal, utilizando as seguintes fórmulas:
#       - para homens : (72.7 * h) – 58
#       - para mulheres : (62.1 * h) – 44.7
# Observação: Altura = h (na fórmula acima)

def peso_ideal(altura: float, sexo: int) -> float:
    if sexo == 1:
        return (72.7 * altura) - 58
    elif sexo == 2:
        return (62.1 * altura) - 44.7
    else:
        raise ValueError('Sexo inválido.')


def main():
    while True:
        try:
            sex: int = int(input('Insira o sexo (1 - feminino, 2 - Masculino): '))
            if sex not in [1, 2]:
                print('Sexo inválido. (1 - feminino, 2 - Masculino)')
            else:
                break
        except ValueError:
            print('Sexo inválido. Digite um número inteiro.')

    while True:
        try:
            altura: float = float(input('Insira a altura em metros. (Ex: 1.75): '))
            if altura > 2.50:
                print('Altura máxima: 2.5m')
            else:
                break
        except ValueError:
            print('Altura inválida.')
    print(f'O peso ideal para {'um homem' if sex == 2 else 'uma mulher'} com {altura}cm é: {peso_ideal(sexo=sex, altura=altura):.2f}')

if __name__ == "__main__":
    main()