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
        
    @property
    def volume_max(self):
        return self.__volume_max

    @volume_max.setter
    def volume_max(self, vol):
        self.__volume_max = vol

    @property
    def volume(self):
        return self.__volume
    
    @property
    def estacao(self):
        return self.__estacao_atual
    
    @property
    def frequencia(self):
        return self.__frequencia_atual

    def __str__(self):
        return (
            f"\n RadioFM:\n"
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
            return False
        else:
            self.__antena_habilitada = True
            return True

    def aumentar_volume(self, vol = 1):
        self.__verificar_status()
        if (self.__volume_min <= vol <= self.__volume_max):
            if (vol == 1):
                self.__volume += vol
            elif (self.__volume + vol <= self.__volume_max):  
                self.__volume += vol 
        else:
            self.__volume = self.__volume_max

    def diminuir_volume(self, vol = 1):
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
    print('# RadioFM')
    entrada = input('Insira um volume máximo para o rádio (ENTER para 100): ')
    volume_max = int(entrada) if entrada.strip() else 100
    radio1 = RadioFM(volume_max, estacoes)

    while True:
        print(radio1)
        print('\nDigite um número:\n1 - Ligar\n2 - Desligar\n3 - Alternar antena\n4 - Aumentar volume\n5 - Diminuir volume\n6 - Aumentar volume máximo\n7 - Mudar frequência\n8 - Sair')
        usuario = str(input('> '))

        if usuario == '1' or usuario.upper() == 'LI':
            radio1.ligar()
            print('## Radio ligado!')

        if usuario == '2' or usuario.upper() == 'DE':
            radio1.desligar()
            print('## Radio desligado!')
            break
            
        if usuario == '3' or usuario.upper() == 'AL':
            print('Status da antena: ', radio1.alternar_antena())

        if usuario == '4' or usuario.upper() == 'AU':
            entrada = input('Qual volume deseja? (ENTER para aumentar 1 nível): ')
            vol = int(entrada) if entrada.strip() else 1
            radio1.aumentar_volume(vol)
            print('Volume atual:', radio1.volume)
            
        if usuario == '5' or usuario.upper() == 'DI':
            entrada = input('Qual volume deseja? (ENTER para diminuir 1 nível): ')
            vol = int(entrada) if entrada.strip() else 1
            radio1.diminuir_volume(vol)
            print('Volume atual:', radio1.volume)

        if usuario == '6' or usuario.upper() == 'AUV':
            entrada = input('Qual volume deseja? (ENTER para aumentar 1 nível): ')
            radio1.volume_max = entrada
            print('Volume atual:', radio1.volume)
            
        if usuario == '7' or usuario.upper() == 'MU':
            print('Estações disponíveis:', estacoes)
            entrada = input('Que frequência deseja? (ENTER para passar para a próxima estação): ')
            freq = float(entrada) if entrada.strip() else 0
            radio1.mudar_frequencia(freq)
            print('Estacao atual:', radio1.estacao, radio1.frequencia)

        if usuario == '8' or usuario.upper() == 'SA':
            print('Saindo...')
            break

if __name__ == "__main__":
    main()
