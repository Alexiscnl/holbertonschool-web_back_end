const fs = require('fs');
const express = require('express');

const app = express();
const port = 1245;
const database = process.argv[2];

function countStudents(path) {
  return new Promise((resolve, reject) => {
    if (!path) return reject(new Error('Cannot load the database'));

    fs.readFile(path, 'utf8', (err, data) => {
      if (err) return reject(new Error('Cannot load the database'));

      const lines = data.trim().split('\n');
      const students = lines.slice(1).filter((line) => line.trim() !== '');

      const fields = {};
      for (const line of students) {
        const parts = line.split(',');
        if (parts.length < 2) continue;

        const firstname = (parts[0] || '').trim();
        const field = (parts[parts.length - 1] || '').trim();

        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstname);
      }

      let text = `Number of students: ${students.length}\n`;

      // tri alphabétique des filières
      const sortedFields = Object.keys(fields).sort();
      for (const field of sortedFields) {
        const list = fields[field].slice().sort();
        text += `Number of students in ${field}: ${list.length}. List: ${list.join(', ')}\n`;
      }

      resolve(text.trim());
    });
  });
}

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  countStudents(database)
    .then((studentsText) => {
      res.send(`This is the list of our students\n${studentsText}`);
    })
    .catch(() => {
      res.send('This is the list of our students\nCannot load the database');
    });
});

app.listen(port);

module.exports = app;
