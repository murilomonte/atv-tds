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
    matricula = str(input())
    nota1 = float(input())
    nota2 = float(input())
    nota3 = float(input())
    mediaExec = float(input())

    print(matricula)
    print(f'{mediaConceito(nota1, nota2, nota3, mediaExec)[0]:.2f}')
    print(mediaConceito(nota1, nota2, nota3, mediaExec)[1])
    print(mediaConceito(nota1, nota2, nota3, mediaExec)[2])

if __name__ == '__main__':
    main()