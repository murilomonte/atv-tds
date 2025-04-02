const express = require('express')
const app = express()
const port = 3000

// ## Configuração de views
// Informa onde estão armazenadas as views
app.set('views', 'views')

// Informa qual engine para renderizar
app.set('view engine', 'ejs')

// ## Configurações do app
// Para somente aceitar objetos simples
app.use(express.urlencoded({ extended: false }))

// ## Métodos para tratar requisições
app.get('/', (req, res) => {
    res.render('home')
})

// Trata a requisição do tipo POST com os dados vindo de /ola
app.post('/resposta_ola', (req, res) => {
    // Acessa o corpo da requisição e obtém o a variável "nome"
    let nome = req.body.nome;
    res.render('resposta', { nome });
});

// Fornecer a página com o formulário
app.get('/ola', (req, res) => {
    res.send(`
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Olá</h1>
    <form action="/resposta_ola" method="post">
        <label for="inome">Nome</label>
        <input type="text" id="inome" name="nome">
    </form>
</body>
</html> 
    `);
});

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
})
