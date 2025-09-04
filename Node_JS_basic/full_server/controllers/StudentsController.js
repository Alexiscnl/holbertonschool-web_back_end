import readDatabase from '../utils';

export default class StudentsController {
  static getAllStudents(req, res) {
    res.status(200).setHeader('Content-Type', 'text/plain');
    const databasePath = process.argv[2];
    readDatabase(databasePath)
      .then((data) => {
        let responseText = 'This is the list of our students\n';
        const fields = Object.keys(data).sort((a, b) => a.localeCompare(b, 'en', { sensitivity: 'base' }));
        for (const f of fields) {
          const students = data[f];
          responseText += `Number of students in ${f}: ${students.length}. List: ${students.join(', ')}\n`;
        }
        res.send(responseText);
      })
      .catch(() => {
        res.status(500).send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(req, res) {
    res.status(200).setHeader('Content-Type', 'text/plain');
    const { major } = req.params;

    if (major !== 'CS' && major !== 'SWE') {
      return res.status(500).send('Major parameter must be CS or SWE');
    }
    const databasePath = process.argv[2];
    readDatabase(databasePath)
      .then((data) => {
        const students = data[major] || [];
        res.send(`List: ${students.join(', ')}`);
      })
      .catch(() => {
        res.status(500).send('Cannot load the database');
      });

    return undefined;
  }
}
