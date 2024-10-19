hora = int(input("").strip())
minuto = int(input("").strip())
segundo = int(input("").strip())

tempoDecorrido = ((hora * 60) * 60) + (minuto * 60) + segundo

print(f"{tempoDecorrido}")