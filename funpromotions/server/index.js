const express = require('express');
const { start } = require('repl');
const app = express();

app.get('/', (req, res)=> {

});

app.get('/concerts', (req, res)=> {

});

app.get('/experience', (req, res)=> {

});
app.get('/about_us', (req, res)=> {

});

app.listen(3000, () => start());