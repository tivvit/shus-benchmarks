let http = require('http');
let fs = require("fs");

let knownUrls = JSON.parse(fs.readFileSync('urls.json', 'utf8'));

let server = http.createServer(function (req, res) {
    let url = req.url.substring(1);
    if (url in knownUrls) {
        res.writeHead(302, {'Location': knownUrls[url]});
    } else {
        res.writeHead(404);
    }
    res.end();
});

server.listen(80);