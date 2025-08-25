<div align="center">
	<h1>🚀 ES6 Data Manipulation 🚀</h1>
	<img src="https://img.shields.io/badge/Node.js-20.x.x-brightgreen" alt="Node.js">
	<img src="https://img.shields.io/badge/Jest-tested-blue" alt="Jest">
	<img src="https://img.shields.io/badge/ESLint-Airbnb%20Base-yellow" alt="ESLint">
</div>

## 📚 Description

Bienvenue dans le projet <b>ES6 Data Manipulation</b> !<br>
Ce projet vous plonge dans la manipulation avancée des structures de données en JavaScript ES6 : Arrays, Typed Arrays, Set, Map et WeakMap.

> <b>Projet proposé par :</b> Johann Kerbrat, Engineering Manager at Uber Works
> <b>Score moyen attendu :</b> 95.65%
> <b>Niveau :</b> Amateur

---

## 🎯 Objectifs pédagogiques

À la fin de ce projet, vous saurez :

- Utiliser efficacement <b>map</b>, <b>filter</b> et <b>reduce</b> sur les tableaux
- Manipuler les <b>Typed Arrays</b>
- Exploiter les structures <b>Set</b>, <b>Map</b> et <b>WeakMap</b>

---

## 🛠️ Prérequis & Exigences

- 🐧 Ubuntu 20.04 LTS
- 🟩 Node.js 20.x.x & npm 9.x.x ou supérieur
- ✏️ Éditeurs : vi, vim, emacs, Visual Studio Code
- 📄 Fichiers en `.js` et terminés par une nouvelle ligne
- 📦 Fonctions exportées, README.md obligatoire
- ✅ Tests avec Jest, lint avec ESLint

---

## ⚡ Installation & Configuration

### 1️⃣ Installer Node.js 20.x.x

```bash
curl -sL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
nodejs -v  # v20.15.1 attendu
npm -v     # 10.7.0 attendu
```

### 2️⃣ Installer Jest, Babel & ESLint

```bash
npm install --save-dev jest
npm install --save-dev babel-jest @babel/core @babel/preset-env
npm install --save-dev eslint
```

### 3️⃣ Configurer le projet

- `package.json` : scripts pour lint, test, dev, full-test
- `babel.config.js` : configuration Babel pour Node.js
- `.eslintrc.js` : configuration ESLint Airbnb + Jest

Après avoir copié les fichiers de configuration :

```bash
npm install
```

---

## 🧰 Scripts utiles

| Commande                   | Description                         |
| -------------------------- | ----------------------------------- |
| `npm run lint`             | Lint du projet                      |
| `npm run check-lint`       | Lint des fichiers JS                |
| `npm run dev <fichier.js>` | Exécuter un fichier avec Babel Node |
| `npm run test`             | Lancer les tests Jest               |
| `npm run full-test`        | Lint + tests                        |

---

## 🏆 Tâches réalisées

<details>
<summary><b>0. Basic list of objects</b></summary>
<ul><li><b>getListStudents</b> : retourne un tableau d'objets étudiants (id, firstName, location).</li></ul>
</details>

<details>
<summary><b>1. More mapping</b></summary>
<ul><li><b>getListStudentIds</b> : retourne un tableau d'ids à partir d'une liste d'étudiants. Utilise <code>map</code>.</li></ul>
</details>

<details>
<summary><b>2. Filter</b></summary>
<ul><li><b>getStudentsByLocation</b> : filtre les étudiants par ville. Utilise <code>filter</code>.</li></ul>
</details>

<details>
<summary><b>3. Reduce</b></summary>
<ul><li><b>getStudentIdsSum</b> : somme des ids des étudiants. Utilise <code>reduce</code>.</li></ul>
</details>

<details>
<summary><b>4. Combine</b></summary>
<ul><li><b>updateStudentGradeByCity</b> : retourne les étudiants d'une ville avec leur nouvelle note (ou 'N/A'). Utilise <code>filter</code> et <code>map</code>.</li></ul>
</details>

<details>
<summary><b>5. Typed Arrays</b></summary>
<ul><li><b>createInt8TypedArray</b> : crée un ArrayBuffer avec une valeur Int8 à une position donnée. Lève une erreur si la position est hors limite.</li></ul>
</details>

<details>
<summary><b>6. Set data structure</b></summary>
<ul><li><b>setFromArray</b> : crée un Set à partir d'un tableau.</li></ul>
</details>

<details>
<summary><b>7. More set data structure</b></summary>
<ul><li><b>hasValuesFromArray</b> : vérifie si tous les éléments d'un tableau sont dans un Set.</li></ul>
</details>

<details>
<summary><b>8. Clean set</b></summary>
<ul><li><b>cleanSet</b> : retourne une chaîne des valeurs du Set commençant par un préfixe donné, séparées par '-'.</li></ul>
</details>

<details>
<summary><b>9. Map data structure</b></summary>
<ul><li><b>groceriesList</b> : retourne une Map des courses (nom, quantité).</li></ul>
</details>

<details>
<summary><b>10. More map data structure</b></summary>
<ul><li><b>updateUniqueItems</b> : met à jour la quantité à 100 pour les items ayant une quantité de 1 dans une Map.</li></ul>
</details>

---

## 📖 Ressources utiles

- [Array](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Global_Objects/Array)
- [Typed Array](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Global_Objects/TypedArray)
- [Set Data Structure](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Global_Objects/Set)
- [Map Data Structure](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Global_Objects/Map)
- [WeakMap](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Global_Objects/WeakMap)

---

<div align="center">
	<b>Projet réalisé dans le cadre du cursus Holberton School.</b><br>
	<i>Bonne manipulation de données ! 🚀</i>
</div>
