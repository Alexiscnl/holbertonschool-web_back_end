export default class AppController {
  static getHomepage(req, res) {
    res.type('text').status(200);
    res.send('Hello Holberton School!');
  }
}
