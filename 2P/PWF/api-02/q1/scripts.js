
class Conversor {
    constructor(base, conversao, res) {
        this.moedaBase = base;
        this.moedaConversao = conversao;
        this.resultado = res
    };

    invertCampos() {
        const temp = this.moedaBase.value;
        this.moedaBase.value = this.moedaConversao.value;
        this.moedaConversao.value = temp;
    }

    clearCampos() {
        this.moedaBase.value = '';
        this.moedaConversao.value = '';
        this.resultado.value = '';
    }

    async consultarPreco() {
        if (this.moedaBase.value == '' || this.moedaConversao.value == '' ) {
            this.resultado.innerHTML = "<p>Preencha os campos<p>";
            throw Error('Campos não preenchidos');
        }
        let url =
            `https://api.binance.com/api/v3/ticker/price?symbol=${this.moedaBase.value.toUpperCase()}${this.moedaConversao.value.toUpperCase()}`;
        try {
            let response = await fetch(url); // Faz a requisição à API Binance
            if (!response.ok) {
                throw new Error(`HTTP Error: ${response.status} - ${response.statusText}`);
            }
            let json = await response.json();

            this.resultado.innerHTML = `
            <p><strong>Par de Moedas:</strong> ${json.symbol}</p>
            <p><strong>Preço:</strong> ${parseFloat(json.price).toFixed(2)}
            ${this.moedaConversao.value.toUpperCase()}</p>`;
        } catch (error) {
            this.resultado.innerHTML = 'Erro: ' + error.message;
        }
    }
}


let moedaConversao = document.getElementById('moedaConversao');
let moedaBase = document.getElementById('moedaBase');
let resultado = document.getElementById('resultado');

let botaoLimpar = document.getElementById('botaoLimpar');
let botaoConsultar = document.getElementById('botaoConsultar');
let botaoInverter = document.getElementById('botaoInverter');

const conversor = new Conversor(moedaBase, moedaConversao, resultado,);

botaoConsultar.addEventListener('click', () => {
    conversor.consultarPreco()
});
botaoLimpar.addEventListener('click',  () => {
    conversor.clearCampos()
});
botaoInverter.addEventListener('click',  () => {
    conversor.invertCampos()
});