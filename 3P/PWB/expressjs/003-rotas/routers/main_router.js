const express = require('express');
const router = express.Router();

// ## Configurações do app
// Para somente aceitar objetos simples
router.use(express.urlencoded({ extended: false }));

// ## Métodos para tratar requisições
router.get('/', (req, res) => {
    res.render('home')
})

// Trata a requisição do tipo POST com os dados vindo de /ola
router.post('/resposta_ola', (req, res) => {
    // Acessa o corpo da requisição e obtém o a variável "nome"
    let nome = req.body.nome;
    res.render('resposta', { nome });
});

// Fornecer a página com o formulário
router.get('/ola', (req, res) => {
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

// ## Métodos para tratar requisições
router.get('/soma', (req, res) => {
    res.render('soma')
})

// Trata a requisição do tipo POST
router.post('/res_soma', (req, res) => {
    // Acessa o corpo da requisição e obtém o a variável "nome"
    let n1 = Number(req.body.n1);
    let n2 = Number(req.body.n2);
    let resposta = n1 + n2;
    res.render('res_soma', { resposta });
});

module.exports = router; 