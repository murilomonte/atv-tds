class Houses {
    async fetchAPI(url) {
        try {
            let response = await fetch(url);

            if (!response.ok) {
                throw new Error(`HTTP Error: ${response.status} - ${response.statusText}`);
            }

            return await response.json();
        } catch (e) {
            console.log("Error:", e);
        }
    }

    async getByName(house, output) {
        let url = `https://wizard-world-api.herokuapp.com/houses`;
        let response = await this.fetchAPI(url);

        for (let result of response) {
            if (result.name == house) {
                output.innerHTML = 
                `<div class="house-item">
                    <p><strong>Nome</strong>: ${result.name}</p>
                    <p><strong>Cores</strong>: ${result.houseColours}</p>
                    <p><strong>Fundador</strong>: ${result.founder}</p>
                    <p><strong>Animal</strong>: ${result.animal}</p>
                    <p><strong>Elemento</strong>: ${result.element}</p>
                    <p><strong>Fantasma</strong>: ${result.ghost}</p>
                    <p><strong>Sala comunal</strong>: ${result.commonRoom}</p>
                    <p><strong>Diretor</strong>: ${result.heads[0].firstName} ${result.heads[0].lastName}</p>
                </div>`;
            }
        }
    }
}


let output = document.getElementById('output');
let searchBtn = document.getElementById('searchBtn');

let houses = new Houses(output);

searchBtn.addEventListener('click', () => {
    let house = document.getElementById('ihouse').value;
    houses.getByName(house, output);
});