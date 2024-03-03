qtDoces = int(input('Qual a quantidade de doces produzidos?: '))
qtCaixas = int(input('Qual a quantidade de caixas disponíveis?: '))

qtCadaCaixa = qtDoces // qtCaixas

print(f'Cada caixa ficará com {qtCadaCaixa} doces.')