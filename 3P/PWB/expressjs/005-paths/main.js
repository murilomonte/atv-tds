const express = require('express')
const app = express()
const port = 3000

const main_router = require('./routers/main_router.js');
const aluno_router = require('./routers/aluno_router.js');

// ## Configuração de views
// Informa onde estão armazenadas as views
app.set('views', 'views');
// Informa qual engine para renderizar
app.set('view engine', 'ejs');
// Utiliza o seguinte diretório para acessar os arquivos estáticos.
app.use(express.static('public'))

app.use('/', main_router)
app.use('/aluno', aluno_router)

app.listen(port, () => {
  console.log(`Example app listening on port http://localhost:${port}`)
})
