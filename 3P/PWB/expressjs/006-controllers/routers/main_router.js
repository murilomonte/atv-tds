const express = require('express');
const router = express.Router();

// ## Configurações do app
// Para somente aceitar objetos simples
router.use(express.urlencoded({ extended: false }));

// ## Métodos para tratar requisições
router.get('/', (req, res) => {
    res.render('index')
})

router.get('/aluno', (req, res) => {
    res.render('aluno/dashboard_aluno')
})

module.exports = router;