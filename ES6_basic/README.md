# ES6 Basics

![Project Badge](https://img.shields.io/badge/ES6%20Basics-Novice-brightgreen)

## Description

Ce projet couvre les bases d'ECMAScript 6 (ES6), une version majeure de JavaScript introduisant de nouvelles fonctionnalités et améliorations. Vous apprendrez à utiliser les nouvelles syntaxes et concepts pour écrire un code plus moderne et efficace.

## Auteur

- Johann Kerbrat, Engineering Manager at Uber Works

## Progression

- Poids : 1
- Votre score sera mis à jour au fur et à mesure de votre progression.

## Ressources

- [ECMAScript 6 - ECMAScript 2015](https://www.ecma-international.org/ecma-262/6.0/)
- [Statements and declarations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements)
- [Arrow functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
- [Default parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters)
- [Rest parameter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters)
- [Javascript ES6 — Iterables and Iterators](https://javascript.info/iterable)

## Objectifs d'apprentissage

À la fin de ce projet, vous serez capable d'expliquer :

- Ce qu'est ES6
- Les nouvelles fonctionnalités introduites dans ES6
- La différence entre une constante et une variable
- Les variables à portée de bloc
- Les fonctions fléchées et les paramètres par défaut
- Les paramètres rest et spread
- Le template string en ES6
- La création d'objets et leurs propriétés en ES6
- Les itérateurs et la boucle for-of

## Exigences

- Tous vos fichiers seront interprétés/compilés sur Ubuntu 20.04 LTS avec node 20.x.x et npm 9.x.x
- Éditeurs autorisés : vi, vim, emacs, Visual Studio Code
- Tous vos fichiers doivent se terminer par une nouvelle ligne
- Un fichier `README.md` à la racine du projet est obligatoire
- Votre code doit utiliser l'extension `.js`
- Votre code sera testé avec Jest
- Votre code sera analysé avec ESLint et des règles spécifiques
- Toutes vos fonctions doivent être exportées

## Installation et configuration

### Installer NodeJS 20.x.x

```bash
curl -sL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
nodejs -v  # Doit afficher v20.15.1
npm -v     # Doit afficher 10.7.0
```

### Installer Jest, Babel et ESLint

```bash
npm install --save-dev jest
npm install --save-dev babel-jest @babel/core @babel/preset-env
npm install --save-dev eslint
```

### Fichiers de configuration requis

- `package.json`
- `babel.config.js`
- `.eslintrc.js`

> **N'oubliez pas d'exécuter** `npm install` **dans le dossier du projet pour installer toutes les dépendances nécessaires.**

> **Ne poussez pas le dossier `node_modules` sur votre dépôt.**
