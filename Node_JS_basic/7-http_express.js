const fs = require('fs');
const express = require('express');

const app = express();
const port = 1245;
const database = process.argv[2];

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        return reject(new Error('Cannot load the database'));
      }
      const lines = data.split('\n');
      const students = lines.slice(1);
      const validStudents = students.filter((line) => line.trim() !== '');
      const fields = {};
      for (const line of validStudents) {
        const parts = line.split(',');
        const firstname = parts[0];
        const field = parts[parts.length - 1];
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstname);
      }
      let text = `Number of students: ${validStudents.length}\n`;
      for (const field in fields) {
        if (Object.prototype.hasOwnProperty.call(fields, field)) {
          const list = fields[field];
          text += `Number of students in ${field}: ${list.length}. List: ${list.join(', ')}\n`;
        }
      }
      return resolve(text.trim());
    });
  });
}

app.get('/', (req, res) => {
  res.end('Hello Holberton School!');
});
app.get('/students', (req, res) => {
  let responseText = 'This is the list of our students\n';
  countStudents(database)
    .then((studentsText) => {
      responseText += studentsText;
      res.end(responseText);
    })
    .catch((error) => {
      res.end(`Error: ${error.message}`);
    });
});
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
});
module.exports = app;
