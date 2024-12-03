from datetime import datetime

def __val_dataHora(momento, formato="%d/%m/%Y %H:%M"):
        try:
            momentoVal = datetime.strptime(momento, formato)
            return momentoVal
        except ValueError:
            raise ValueError("Data e hora inválidas!")
        
entrada = __val_dataHora("12/07/2024 20:25")
saida = __val_dataHora("13/07/2024 20:25")

total = (saida - entrada).total_seconds() / 60

print(total)

if total > 120:
    restante = (total - 120) / 15
    totalPag = (restante * 0.5) + 8
else:
    totalPag = 8
print(totalPag)

# print('hora', total // 60)
# print('minuto', total % 60)