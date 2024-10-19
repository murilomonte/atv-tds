# A 	>= 9.0
# B 	>= 7.5 e < 9.0
# C 	>= 6.0 e < 7.5
# D 	>= 4.0 e < 6.0
# E 	< 4.0

def mediaConceito(nota1, nota2, nota3, mediaExec):
    mediaFinal = (nota1 + nota2 * 2 + nota3 * 3 + mediaExec) / 7

    if mediaFinal < 4: 
        conceito = 'E'
    elif mediaFinal < 6:
        conceito = 'D'
    elif mediaFinal < 7.5:
        conceito = 'C'
    elif mediaFinal < 9:
        conceito = 'B'
    else:
        conceito = 'A'

    if conceito == 'A' or conceito == 'B' or conceito == 'C':
        situacaoFinal = 'Aprovado'
    else:
        situacaoFinal = 'Reprovado'

    return mediaFinal, conceito, situacaoFinal

def main():
    matricula = str(input('Insira a matrícula do aluno: '))
    nota1 = float(input('Insira a primeira nota: '))
    nota2 = float(input('Insira a segunda nota: '))
    nota3 = float(input('Insira a terceira nota: '))
    mediaExec = float(input('Insira a terceira nota: '))

    print(matricula)
    print(f'{mediaConceito(nota1, nota2, nota3, mediaExec)[0]:.2f}')
    print(mediaConceito(nota1, nota2, nota3, mediaExec)[1])
    print(mediaConceito(nota1, nota2, nota3, mediaExec)[2])

if __name__ == '__main__':
    main()