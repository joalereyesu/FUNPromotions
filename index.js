const express = require('express');
const { start } = require('repl');
const app = express();

app.get('/', (req, res)=> {

});

app.listen(3000, () => start());