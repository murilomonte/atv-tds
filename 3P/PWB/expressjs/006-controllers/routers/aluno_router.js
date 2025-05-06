const express = require('express');
const router = express.Router();

let registros = [];

// ## Configurações do app
// Para somente aceitar objetos simples
router.use(express.urlencoded({ extended: false }));


router.get('/historico', (req, res) => {
    res.render('aluno/historico', {registros})
})

router.get('/novo_registro', (req, res) => {
    res.render('aluno/novo_registro')
})

router.post('/novo_registro', (req, res) => {
    let response = req.body;

    let disciplina = response.disciplina;
    let nota1 = Number(response.nota1);
    let nota2 = Number(response.nota2);

    let media = (nota1 + nota2) / 2;

    let registro = {
        disciplina: disciplina,
        nota1: nota1,
        nota2: nota2,
        media: media
    };

    registros.push(registro);

    res.render('historico', { registros });
})

module.exports = router;