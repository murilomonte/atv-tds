const express = require('express');
const app = express();
const port = 3000;
const main_router = require('./routers/main_routers.js');

// ## Configuração de views
// Informa onde estão armazenadas as views
app.set('views', 'views');

// Informa qual engine para renderizar
app.set('view engine', 'ejs');

// Redireciona todas as requisições para o roteador 
app.use('/', main_router);

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
})
