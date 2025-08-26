# ES6 Promises ![Amateur Badge](https://img.shields.io/badge/Level-Amateur-blue)

> **By:** Johann Kerbrat, Engineering Manager at Uber Works
> **Weight:** 1

---

## 🚀 Description

This project explores **ES6 Promises** in JavaScript, focusing on asynchronous programming, error handling, and modern async/await syntax. Your score will be updated as you progress!

---

## 📚 Resources

- [MDN: Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
- [JavaScript Promise: An introduction](https://developers.google.com/web/fundamentals/primers/promises)
- [MDN: Await](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await)
- [MDN: Async](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)
- [MDN: Throw / Try](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/throw)

---

## 🎯 Learning Objectives

By the end of this project, you should be able to explain:

- What are Promises (how, why, and what)?
- How to use `then`, `resolve`, `catch` methods
- How to use every method of the `Promise` object
- How to use `throw` / `try`
- The `await` operator
- How to use an `async` function

---

## ✅ Requirements

- All files interpreted/compiled on **Ubuntu 20.04 LTS** using **Node 20.x.x** and **npm 9.x.x**
- Allowed editors: `vi`, `vim`, `emacs`, **Visual Studio Code**
- All files must end with a new line
- A `README.md` file at the root of the project is mandatory
- Use the `.js` extension for all code
- Code will be tested using **Jest** (`npm run test`)
- Code will be verified with **ESLint**
- All functions must be exported

---

## 🛠️ Setup

### 1. Install NodeJS 20.x.x

```bash
curl -sL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
nodejs -v   # Should output v20.15.1
npm -v      # Should output 10.7.0
```

### 2. Install Jest, Babel, and ESLint

```bash
npm install --save-dev jest
npm install --save-dev babel-jest @babel/core @babel/preset-env @babel/cli
npm install --save-dev eslint
```

---

## 📦 Files & Scripts

### `package.json` (scripts section)

```json
{
  "scripts": {
    "lint": "./node_modules/.bin/eslint",
    "check-lint": "lint [0-9]*.js",
    "dev": "npx babel-node",
    "test": "jest",
    "full-test": "./node_modules/.bin/eslint [0-9]*.js && jest"
  }
}
```

### `babel.config.js`

```js
module.exports = {
  presets: [
    [
      "@babel/preset-env",
      {
        targets: {
          node: "current",
        },
      },
    ],
  ],
};
```

### `utils.js` (example)

```js
export function uploadPhoto() {
  return Promise.resolve({
    status: 200,
    body: "photo-profile-1",
  });
}

export function createUser() {
  return Promise.resolve({
    firstName: "Guillaume",
    lastName: "Salva",
  });
}
```

---

## 🧪 Response Data Format

- **uploadPhoto** returns:
  ```json
  {
    "status": 200,
    "body": "photo-profile-1"
  }
  ```
- **createUser** returns:
  ```json
  {
    "firstName": "Guillaume",
    "lastName": "Salva"
  }
  ```

---

## ⚡ Pro Tips

- Don’t forget to run `$ npm install` after updating `package.json`!
- Use `npm run full-test` to lint and test your code in one go.

---

Happy coding! 🚀
