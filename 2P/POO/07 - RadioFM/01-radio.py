estacoes = {89.5: 'Cocais', 91.5: 'Mix', 94.1: 'Boa', 99.1: 'Clube'}

class RadioFM:
    def __init__(self, vol_max, estacoes):
        self.__volume_min = 0
        self.__volume_max = vol_max
        self.__freq_min = 88
        self.__freq_max = 108
        self.__estacoes = estacoes
        self.__estacoes_tupla = list(estacoes.items())
        self.__volume = None
        self.__ligado = False
        self.__estacao_atual = None
        self.__frequencia_atual = None
        self.__antena_habilitada = False

    def __str__(self):
        return (
            f"RadioFM:\n"
            f"  volume_min: {self.__volume_min}\n"
            f"  volume_max: {self.__volume_max}\n"
            f"  freq_min: {self.__freq_min}\n"
            f"  freq_max: {self.__freq_max}\n"
            f"  volume: {self.__volume}\n"
            f"  ligado: {self.__ligado}\n"
            f"  estação_atual: {self.__estacao_atual}\n"
            f"  frequência_atual: {self.__frequencia_atual}\n"
            f"  antena_habilitada: {self.__antena_habilitada}"
        )
    
    def __verificar_status(self):
        if self.__ligado == False:
            raise ValueError('Você não pode fazer isso enquanto o radio estiver desligado')
            
    def ligar(self):
        self.__ligado = True
        self.__volume = self.__volume_min
        self.__frequencia_atual = self.__estacoes_tupla[0][0]
        self.__estacao_atual = self.__estacoes_tupla[0][1]
        self.alternar_antena()
        if self.__antena_habilitada == True:
            self.__frequencia_atual = self.__estacoes_tupla[0][0]
            self.__estacao_atual = self.__estacoes_tupla[0][1]

    def desligar(self):
        self.__ligado = False
        self.__volume = None
        self.__frequencia_atual = None
        self.alternar_antena()
        self.__estacao_atual = None

    def alternar_antena(self):
        if self.__antena_habilitada:
            self.__antena_habilitada = False
        else:
            self.__antena_habilitada = True

    def aumentar_volume(self, vol = 1):
        self.__verificar_status()
        if (self.__volume_min <= vol <= self.__volume_max):
            if (vol == 1):
                self.__volume += vol
            elif (self.__volume + vol <= self.__volume_max):  
                self.__volume += vol 
        else:
            self.__volume = self.__volume_max

    def diminuir_volume(self, vol = 0):
        self.__verificar_status()
        if (self.__volume_min <= vol <= self.__volume_max):
            if (vol == 1):
                self.__volume -= vol
            elif (self.__volume - vol <= self.__volume_min):  
                self.__volume += vol 
        else:
            self.__volume = self.__volume_min

    def mudar_frequencia(self, freq = 0):
        self.__verificar_status()
        if (freq != 0):
            if (freq in self.__estacoes):
                self.__frequencia_atual = freq
                self.__estacao_atual = self.__estacoes[freq]
            else:
                raise ValueError('Estação inválida')
        else:
            indice_atual = self.__estacoes_tupla.index(
                (self.__frequencia_atual, self.__estacao_atual)
            )
            indice_atual += 1
            if indice_atual > len(self.__estacoes_tupla) - 1:
                indice_atual = 0
            self.__frequencia_atual = self.__estacoes_tupla[indice_atual][0]
            self.__estacao_atual = self.__estacoes_tupla[indice_atual][1]

def main():
    radio1 = RadioFM(100, estacoes)
    radio1.ligar()
    radio1.aumentar_volume()
    radio1.diminuir_volume()
    radio1.mudar_frequencia()
    print(radio1)
    radio1.desligar()

if __name__ == "__main__":
    main()
