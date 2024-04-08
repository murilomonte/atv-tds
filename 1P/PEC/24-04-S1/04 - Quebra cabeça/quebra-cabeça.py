# separar.png
# Função que recebe uma data no formato DDMMYYYY e devolve cada dado separadamente.
def separar_data(dma):
    # A variável 'a' recebe o valor referente a data.
    a = dma % 10000
    
    # A variável 'dma' recebe a divisão inteira.
    dma //= 10000
    
    # A variável 'm' recebe o valor ferente ao mês.
    m = dma % 100
    
    # A variável 'dma' recebe a divisão inteira.
    dma //= 100
    
    # A variável 'd' recebe o valor referente ao ano.
    d = dma

    # A função retorna os valores separadamente.
    return d, m, a

# signo.png
# Função que determina o signo a partir de uma data informada.
def signo(dia, mes):
    # Se o mês atender a condição.
    if mes == 3:
        # A função retorna o signo referente ao dia.
        return "Peixes" if dia < 21 else "Áries"
    if mes == 4:
        return "Áries" if dia < 20 else "Touro"
    if mes == 5:
        return "Touro" if dia < 21 else "Gêmeos"
    if mes == 6:
        return "Gêmeos" if dia < 22 else "Câncer"
    if mes == 7:
        return "Câncer" if dia < 23 else "Leão"
    if mes == 8:
        return "Leão" if dia < 23 else "Virgem"
    if mes == 9:
        return "Virgem" if dia < 23 else "Libra"
    if mes == 10:
        return "Libra" if dia < 23 else "Escorpião"
    if mes == 11:
        return "Escorpião" if dia < 22 else "Sagitário"
    if mes == 12:
        return "Sagitário" if dia < 22 else "Capricórnio"
    if mes == 1:
        return "Capricórnio" if dia < 20 else "Aquário"
    if mes == 2:
        return "Aquário" if dia < 19 else "Peixes"

# remover.png
# Função que remove o acento de um texto.
def remover_acentos(texto):
    # Importa a função 'normalize' do módulo 'unicodedata'.
    from unicodedata import normalize

    # Retorna o texto sem acentos.
    return normalize("NFKD", texto).encode("ASCII", "ignore").decode("ASCII")

# horoscopo.png
# Função que obtém o horóscopo do dia para um signo informado.
def horoscopo(signo_desejado):
    # Importa o módulo urllib.request
    import urllib.request

    # Guarda o valor recebido pela função 'remover_acentos' passando como parâmetro um determinado signo.
    signo_formatado = remover_acentos(signo_desejado).lower()

    # Guarda uma url concatenada com o signo informado
    minha_url = "https://www.horoscopovirtual.com.br/horoscopo/" + signo_formatado
    
    requisicao = urllib.request.Request(
        url=minha_url, headers={"User-Agent": "Mozilla/5.0"}
    )
    resposta = urllib.request.urlopen(requisicao)
    pagina = resposta.read().decode("utf-8")
    marcador_inicio = '<p class="text-pred">'
    marcador_final = "</p>"

    inicio = pagina.find(marcador_inicio) + len(marcador_inicio)
    final = pagina.find(marcador_final, inicio)

    return signo_desejado + ": " + pagina[inicio:final]

# main.png
# Função principal onde se encontra os comandos principais do código.
def main():
    # A variável 'nascimento' recebe o nascimento informado pelo usuário.
    nascimento = int(input("Digite sua data de nascimento no formato DDMMAAAA: "))
    
    # As variáveis recebem o valor retornado das funções
    dia, mes, _ = separar_data(nascimento)
    meu_signo = signo(dia, mes)
    horoscopo_de_hoje = horoscopo(meu_signo)

    # É mostrado na tela o resultado na tela.
    print(horoscopo_de_hoje)

# name.png
# Condição que avalia qual é o módulo principal do script atual.
if __name__ == "__main__":
    main()