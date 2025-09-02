const express = require('express');
const fs = require('fs');

const app = express();
const port = 1245;

const DB_PATH = process.argv[2];

function parseStudents(data) {
  const lines = data
    .split('\n')
    .map((l) => l.trim())
    .filter((l) => l.length > 0);

  if (lines.length <= 1) {
    return { total: 0, order: [], groups: {} };
  }

  const header = lines[0];
  const rows = lines.slice(1);
  const cols = header.split(',').map((c) => c.trim());
  const idxFirst = cols.indexOf('firstname');
  const idxField = cols.indexOf('field');
  const groups = Object.create(null);
  const order = [];
  let total = 0;
  for (const row of rows) {
    const cells = row.split(',').map((c) => c.trim());
    const firstname = cells[idxFirst];
    const field = cells[idxField];
    if (!groups[field]) {
      groups[field] = [];
      order.push(field);
    }
    groups[field].push(firstname);
    total += 1;
  }

  return { total, order, groups };
}

app.get('/', (req, res) => {
  res.set('Content-Type', 'text/plain');
  res.status(200).send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  res.set('Content-Type', 'text/plain');
  let body = 'This is the list of our students\n';
  fs.readFile(DB_PATH, 'utf8', (err, data) => {
    if (err) {
      body += 'Cannot load the database';
      res.type('text/plain').status(200).send(body);
      return;
    }
    const { total, order, groups } = parseStudents(data);
    body += `Number of students: ${total}\n`;
    for (const field of order) {
      const count = groups[field].length;
      const list = groups[field].join(', ');
      body += `Number of students in ${field}: ${count}. List: ${list}\n`;
    }
    res.type('text/plain').status(200).send(body);
  });
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
});
module.exports = app;
