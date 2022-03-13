'use strict';

let express = require('express');
let fs = require("fs");

let knownUrls = JSON.parse(fs.readFileSync('urls.json', 'utf8'));

const PORT = 80;
const HOST = '0.0.0.0';

const app = express();
app.get('/:short', (req, res) => {
    let url = req.params["short"];
    if (url in knownUrls) {
        res.redirect(knownUrls[url]);
    } else {
        res.status(404).send();
    }
});

app.listen(PORT, HOST);
