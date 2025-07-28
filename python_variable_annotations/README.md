# 🐍 Python - Variable Annotations

Bienvenue dans ce projet sur les **annotations de type en Python 3** !
Ici, tu vas découvrir comment rendre ton code plus lisible, robuste et maintenable grâce au typage statique.

---

## 🚀 Objectifs pédagogiques

À la fin de ce projet, tu sauras :
- ✅ Utiliser les annotations de type en Python 3
- ✅ Spécifier les types des variables et des signatures de fonctions
- ✅ Comprendre le duck typing
- ✅ Valider ton code avec `mypy`

---

## 📚 Ressources utiles

- [Documentation officielle Python typing](https://docs.python.org/3/library/typing.html)
- [MyPy cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)

---

## 📝 Exigences

- Éditeurs autorisés : `vi`, `vim`, `emacs`
- Python 3.9 sur Ubuntu 20.04 LTS
- Tous les fichiers doivent commencer par `#!/usr/bin/env python3`
- Respect du style `pycodestyle` (2.5)
- Documentation complète pour chaque module, fonction et classe
- Tous les fichiers doivent être exécutables

---

## 🗂️ Fichiers du projet

| Fichier                      | Description                                      |
|------------------------------|--------------------------------------------------|
| `0-add.py`                   | Addition de deux floats avec annotations         |
| `1-concat.py`                | Concaténation de deux chaînes                    |
| `2-floor.py`                 | Partie entière d'un float                        |
| `3-to_str.py`                | Conversion d'un float en string                  |
| `4-define_variables.py`      | Déclaration de variables typées                  |
| `5-sum_list.py`              | Somme d'une liste de floats                      |
| `6-sum_mixed_list.py`        | Somme d'une liste mixte (int et float)           |
| `7-to_kv.py`                 | Tuple clé/valeur avec carré d'un nombre          |
| `8-make_multiplier.py`       | Générateur de fonctions multiplicatrices         |
| `9-element_length.py`        | Duck typing : longueur des éléments d'un itérable|

---

## 💡 Exemples d'annotations

```python
def add(a: float, b: float) -> float:
    """Additionne deux nombres à virgule flottante."""
    return a + b

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Calcule la somme d'une liste mixte."""
    return sum(mxd_lst)
```

---

## 🧪 Tester ton code

Chaque fichier peut être testé avec son fichier main associé :

```bash
./0-main.py
./1-main.py
./2-main.py
# etc.
```

---

## 🎨 Style et vérification

- **Style** :
  ```bash
  pycodestyle *.py
  ```
- **Typage** :
  ```bash
  mypy *.py
  ```

---

## 👨‍💻 Auteur

Projet réalisé par **Emmanuel Turlay**
Pour le cursus Holberton School

---

> **Astuce :** Les annotations de type rendent ton code plus sûr et plus facile à maintenir. Utilise-les partout où tu peux !

---

✨ **Bon code !** ✨
