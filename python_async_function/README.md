# 🚀 Python Async Function

Bienvenue dans ce projet sur la **programmation asynchrone en Python 3** !
Découvre comment créer des coroutines, gérer des tâches concurrentes, et optimiser les performances avec `asyncio`.

---

## 🎯 Objectifs pédagogiques

À la fin de ce projet, tu sauras :

- ✅ Utiliser la syntaxe `async` et `await` en Python
- ✅ Créer et exécuter des coroutines asynchrones
- ✅ Gérer plusieurs tâches en parallèle avec `asyncio`
- ✅ Mesurer les performances d'exécution asynchrone
- ✅ Utiliser `asyncio.Task` pour une meilleure gestion des tâches

---

## 📚 Ressources utiles

- [Documentation officielle asyncio](https://docs.python.org/3/library/asyncio.html)
- [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/)
- [Python Coroutines and Tasks](https://docs.python.org/3/library/asyncio-task.html)

---

## 📝 Exigences

- **Environnement** : Python 3.9 sur Ubuntu 20.04 LTS
- **Style** : Respect du `pycodestyle`
- **Shebang** : Tous les fichiers doivent commencer par `#!/usr/bin/env python3`
- **Documentation** : Docstrings pour chaque fonction
- **Exécutables** : Tous les fichiers doivent être exécutables

---

## 🗂️ Fichiers du projet

| Fichier                      | Description                                       |
| ---------------------------- | ------------------------------------------------- |
| `0-basic_async_syntax.py`    | 🔄 Coroutine basique avec délai aléatoire         |
| `1-concurrent_coroutines.py` | ⚡ Exécution concurrente de plusieurs coroutines  |
| `2-measure_runtime.py`       | ⏱️ Mesure du temps d'exécution asynchrone         |
| `3-tasks.py`                 | 📋 Création d'asyncio.Task à partir de coroutines |
| `4-tasks.py`                 | 🔄 Version avec Tasks de l'exécution concurrente  |

---

## 💡 Exemples d'utilisation

### **Coroutine basique :**

```python
import asyncio
from basic_async_syntax import wait_random

# Attend un délai aléatoire et retourne sa valeur
result = asyncio.run(wait_random(5))
print(f"Délai attendu : {result} secondes")
```

### **Exécution concurrente :**

```python
import asyncio
from concurrent_coroutines import wait_n

# Lance 5 coroutines en parallèle
delays = asyncio.run(wait_n(5, 10))
print(f"Délais triés : {delays}")
```

### **Mesure de performance :**

```python
from measure_runtime import measure_time

# Mesure le temps moyen par coroutine
avg_time = measure_time(5, 9)
print(f"Temps moyen : {avg_time} secondes")
```

### **Gestion avec Tasks :**

```python
import asyncio
from tasks import task_wait_random

# Crée une tâche asyncio
task = task_wait_random(5)
result = asyncio.run(task)
print(f"Résultat de la tâche : {result}")
```

---

## 🧪 Tester le code

Chaque exercice a son fichier de test :

```bash
# Test exercice 0
./0-main.py

# Test exercice 1
./1-main.py

# Test exercice 2
./2-main.py

# Test exercice 3
./3-main.py

# Test exercice 4
./4-main.py
```

---

## 🎨 Vérification du style

```bash
# Vérifier le style de code
pycodestyle *.py

# Rendre les fichiers exécutables
chmod +x *.py
```

---

## 🔍 Concepts clés appris

- **`async def`** : Déclarer une coroutine
- **`await`** : Attendre l'exécution d'une coroutine
- **`asyncio.run()`** : Lancer une coroutine depuis du code synchrone
- **`asyncio.sleep()`** : Pause asynchrone non-bloquante
- **`asyncio.as_completed()`** : Itérer sur les tâches terminées
- **`asyncio.create_task()`** : Créer une tâche asyncio
- **Concurrence vs Parallélisme** : Exécution simultanée de tâches

---

## 👨‍💻 Auteur

Projet réalisé dans le cadre du cursus **Holberton School**
Focus sur la programmation asynchrone et les performances

---

> **💡 Astuce :** La programmation asynchrone est idéale pour les opérations I/O (réseau, fichiers, bases de données). Elle permet d'améliorer significativement les performances !

---

✨ **Bon apprentissage de l'asynchrone !** ✨
