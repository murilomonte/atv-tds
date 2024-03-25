frase =  str(input('Digite uma frase: ').strip())

def contadorDeLetras(frase):
    return len(frase)

print(f"A frase: {frase}\nTem o comprimento de {contadorDeLetras(frase)} letras")