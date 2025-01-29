class Itunes {
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

    async getArtistId(artist) {
        let artistName = artist;
        artist = artist.toString().replace(' ', '+');
        let url = `https://itunes.apple.com/search?term=${artist}`;

        let json = await this.fetchAPI(url)

        for (let result of json.results) {
            if (result.artistName.toUpperCase() == artistName.toUpperCase()) {
                return result.artistId
            }
        }
    }

    async getAlbum(artist, output) {
        if (artist == '') {
            output.innerHTML = `<p>Informe um artista.</p>`;
            throw new Error("Informe um artista.");
        }

        let artistId = await this.getArtistId(artist)
        let url = `https://itunes.apple.com/lookup?id=${artistId}&entity=album`;

        let json = await this.fetchAPI(url)

        output.innerHTML = '';
        for (let result of json.results.slice(1)) {
            output.innerHTML += `
            <div class="album-item">
                <div class="album-image">
                    <img src="${result.artworkUrl100}">
                </div>
                <div class="album-info">
                    <p><strong>Nome</strong>: ${result.collectionName}</p>
                    <p><strong>Quantidade de músicas</strong>: ${result.trackCount}</p>
                    <p><strong>Data de lançamento</strong>: ${result.releaseDate}</p>
                    <p><strong>Gênero musical</strong>: ${result.primaryGenreName}</p>
                </div>
            </div>`
        }
    }
}

let output = document.getElementById('output');
let searchBtn = document.getElementById('searchBtn');

let itunes = new Itunes(output);

searchBtn.addEventListener('click', () => {
    let artist = document.getElementById('iartist').value;
    itunes.getAlbum(artist, output)
});