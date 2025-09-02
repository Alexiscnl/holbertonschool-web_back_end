const http = require('http');
const url = require('url');
const countStudents = require('./3-read_file_async');

const app = http.createServer(async (req, res) => {
  const reqUrl = url.parse(req.url).pathname;
  if (reqUrl === '/') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello Holberton School!');
  } else if (reqUrl === '/students') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    const path = process.argv[2];
    let output = '';
    const originalLog = console.log;
    console.log = (msg) => { output += `${msg}\n`; };
    try {
      await countStudents(path);
    } catch (err) {
      console.log = originalLog;
      res.end('This is the list of our students\nCannot load the database');
      return;
    }
    console.log = originalLog;
    output = output.trimEnd();
    res.end(`This is the list of our students\n${output}`);
  }
});
app.listen(1245);
module.exports = app;
