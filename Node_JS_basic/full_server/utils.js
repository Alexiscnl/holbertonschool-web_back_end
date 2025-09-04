const fs = require('fs');

function readDatabase(path) {
  return new Promise((resolve, reject) => { // eslint-disable-line consistent-return
    if (!path) {
      return reject(new Error('Cannot load the database'));
    }
    fs.readFile(path, 'utf8', (error, data) => {
      if (error) {
        return reject(new Error('Cannot load the database'));
      }
      const studentline = data.split('\n');
      const students = studentline.slice(1);
      const validStudents = students.filter((line) => line.trim() !== '');
      const studentsByField = {};

      for (const studentline of validStudents) {
        const parts = studentline.split(',');
        const firstname = parts[0];
        const field = parts[parts.length - 1];

        if (!studentsByField[field]) {
          studentsByField[field] = [];
        }
        studentsByField[field].push(firstname);
      }
      return resolve(studentsByField);
    });
  });
}
module.exports = readDatabase;
