def contCar(nome, conj = ''):
    return len(nome + conj)

nome = str(input('Qual o seu nome?: '))
estCiv = str(input('Qual seu estado civil?: (1 - Casado(a); 2 - Solteiro(a)): '))

if (estCiv == '1'):
    conj = str(input('Qual o nome do cônjugue?: '))
    print(contCar(nome, conj))
else:
    print(contCar(nome))
    