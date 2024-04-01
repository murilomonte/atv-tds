def contCar(nome, conj = ''):
    return len(nome + conj)

nome = str(input('').strip())
estCiv = str(input('').strip())

if (estCiv == '1'):
    conj = str(input('').strip())
    print(contCar(nome, conj))
else:
    print(contCar(nome))
    