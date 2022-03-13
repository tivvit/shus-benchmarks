'use strict';

let express = require('express');
let fs = require("fs");

let knownUrls = JSON.parse(fs.readFileSync('urls.json', 'utf8'));

const PORT = 80;
const HOST = '0.0.0.0';

const app = express();
for (const [short, target] of Object.entries(knownUrls)) {
    app.get('/' + short, (req, res) => {
        res.redirect(target);
    });
}

app.get('/*', (req, res) => {
    res.status(404).send();
});

console.log("loaded");

app.listen(PORT, HOST);
