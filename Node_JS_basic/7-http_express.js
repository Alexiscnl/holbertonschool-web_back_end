const express = require('express');
const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim());
      if (lines.length <= 1) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const columns = lines[0].split(',');
      const fieldIndex = columns.indexOf('field');
      const firstnameIndex = columns.indexOf('firstname');

      const students = lines.slice(1);
      const fields = {};

      students.forEach((student) => {
        const values = student.split(',');
        const field = values[fieldIndex];
        const firstname = values[firstnameIndex];

        fields[field] = fields[field] || [];
        fields[field].push(firstname);
      });

      let report = `Number of students: ${students.length}`;
      Object.keys(fields).forEach((field) => {
        report += `\nNumber of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`;
      });

      resolve(report);
    });
  });
}

const app = express();
const port = 1245;

app.get('/', (req, res) => {
  res.set('Content-Type', 'text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  res.set('Content-Type', 'text/plain');
  const databaseFilename = process.argv[2];

  try {
    const report = await countStudents(databaseFilename);
    res.send(`This is the list of our students\n${report}`);
  } catch (error) {
    res.send(`This is the list of our students\n${error.message}`);
  }
});

app.listen(port);

module.exports = app;
