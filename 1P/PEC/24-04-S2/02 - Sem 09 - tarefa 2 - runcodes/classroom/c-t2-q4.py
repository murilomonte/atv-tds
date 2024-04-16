# Um sacolão está vendendo frutas com a seguinte tabela de preços:

# Item 	    Até 5Kg 	Acima de 5Kg
# Morango 	R$ 2,50 	R$ 2,20        
# Maça 	    R$ 1,80 	R$ 1,50

# total > 8kg or valor > R$25 then valor total - 10%

# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um programa que leia a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.


def sacolao(morangoPeso, macaPeso):
    morangoVal = 2.50
    macaVal = 1.80

    if morangoPeso > 5:
        morangoVal = 2.20
    if macaPeso > 5:
        macaVal = 1.50
    
    valorTotal = (morangoVal * morangoPeso) + (macaVal * macaPeso)
    pesoTotal = morangoPeso + macaPeso

    if pesoTotal > 8 or valorTotal > 25:
        valorTotal = valorTotal - (valorTotal * 10/100)
    
    return valorTotal

def main():
    morango = float(input('Quantos kg de morango?: '))
    maca = float(input('Quantos kg maca?: '))

    print(f'Valor total: {sacolao(morango, maca):.2f}')
    
if __name__ == '__main__':
    main()
