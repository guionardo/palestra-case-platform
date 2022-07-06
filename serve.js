const fs = require('fs'),
    http = require('http'),
    path = require('path'),
    mimes = {
        '.html': 'text/html',
        '.css': 'text/css',
        '.js': 'application/javascript',
        '.json': 'application/json',
        '.png': 'image/png',
        '.jpg': 'image/jpeg',
        '.gif': 'image/gif',
        '.svg': 'image/svg+xml',
        '.webp': 'image/webp',
    }

console.log('Starting server... http://localhost:8080')
http.createServer((req, res) => {
    if (req.url === '/') {
        res.writeHead(200, { 'Content-Type': 'text/html' })
        res.end(fs.readFileSync('index.html'))
        return
    }
    fs.readFile('pack' + req.url, (err, data) => {
        if (err) {
            console.error(`Error ${req.url}: ${err}`)
            res.writeHead(404);
            res.end(JSON.stringify(err));
            return;
        }
        console.log(`200 ${req.url}`);
        const ext = path.extname(req.url)
        res.writeHead(200, { 'Content-Type': mimes[ext] || 'text/html' })
        res.end(data);
    })
}).listen(8080)