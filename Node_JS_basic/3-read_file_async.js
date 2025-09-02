const fs = require('fs');

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
      console.log(`Number of students: ${validStudents.length}`);
      for (const field in fields) {
        if (Object.prototype.hasOwnProperty.call(fields, field)) {
          const list = fields[field];
          console.log(`Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`);
        }
      }

      return resolve();
    });
  });
}
module.exports = countStudents;
