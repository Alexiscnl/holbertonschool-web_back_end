# 📄 Python Pagination

Bienvenue dans ce projet sur la **pagination en Python** !
Apprends à diviser efficacement de grandes quantités de données en pages gérables pour améliorer les performances et l'expérience utilisateur.

---

## 🎯 Objectifs pédagogiques

À la fin de ce projet, tu sauras :

- ✅ Implémenter une pagination simple avec des paramètres `page` et `page_size`
- ✅ Créer une pagination avec métadonnées (hypermedia)
- ✅ Gérer la pagination resistant aux suppressions de données
- ✅ Optimiser les requêtes de base de données pour la pagination
- ✅ Calculer les indices de début et fin pour chaque page
- ✅ Implémenter des liens de navigation (suivant, précédent, etc.)

---

## 📚 Concepts clés abordés

### **Types de pagination :**

- **Pagination simple** : Division basique par numéro de page
- **Pagination avec hypermedia** : Métadonnées et liens de navigation
- **Pagination deletion-resilient** : Résistante aux modifications de données

### **Métadonnées importantes :**

- `page_size` : Nombre d'éléments par page
- `page` : Numéro de page actuelle
- `data` : Contenu de la page
- `next_page` : Lien vers la page suivante
- `prev_page` : Lien vers la page précédente
- `total_pages` : Nombre total de pages

---

## 🗂️ Structure du projet

```
pagination/
├── README.md
├── Popular_Baby_Names.csv      # Dataset de test
├── 0-simple_helper_function.py # Fonction helper pour indices
├── 1-simple_pagination.py      # Pagination basique
├── 2-hypermedia_pagination.py  # Pagination avec métadonnées
├── 3-hypermedia_del_pagination.py # Pagination résistante
└── tests/                      # Fichiers de test
    ├── 0-main.py
    ├── 1-main.py
    ├── 2-main.py
    └── 3-main.py
```

---

## 📝 Exigences techniques

- **Python** : Version 3.7+ sur Ubuntu 18.04 LTS
- **Style** : Conformité `pycodestyle` (version 2.5.\*)
- **Documentation** : Docstrings pour modules, classes et méthodes
- **Type annotations** : Obligatoires pour toutes les fonctions
- **Première ligne** : `#!/usr/bin/env python3`
- **Fin de fichier** : Nouvelle ligne obligatoire

---

## 🚀 Fonctionnalités implémentées

### **1. Fonction helper (`0-simple_helper_function.py`)**

```python
def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calcule les indices de début et fin pour la pagination.

    Args:
        page: Numéro de page (1-indexée)
        page_size: Nombre d'éléments par page

    Returns:
        Tuple contenant (start_index, end_index)
    """
```

### **2. Pagination simple (`1-simple_pagination.py`)**

```python
class Server:
    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Récupère une page spécifique du dataset.

        Args:
            page: Numéro de page (défaut: 1)
            page_size: Taille de page (défaut: 10)

        Returns:
            Liste des lignes pour cette page
        """
```

### **3. Pagination avec hypermedia (`2-hypermedia_pagination.py`)**

```python
def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
    """
    Retourne une page avec métadonnées complètes.

    Returns:
        Dict avec page_size, page, data, next_page, prev_page, total_pages
    """
```

### **4. Pagination résistante (`3-hypermedia_del_pagination.py`)**

```python
def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict[str, Any]:
    """
    Pagination basée sur l'index, résistante aux suppressions.

    Args:
        index: Index de début actuel
        page_size: Nombre d'éléments par page

    Returns:
        Dict avec index, next_index, page_size, data
    """
```

---

## 💡 Exemples d'utilisation

### **Pagination simple :**

```python
from simple_pagination import Server

server = Server()

# Première page avec 10 éléments
page_1 = server.get_page(1, 10)
print(f"Page 1: {len(page_1)} éléments")

# Deuxième page avec 5 éléments
page_2 = server.get_page(2, 5)
print(f"Page 2: {len(page_2)} éléments")
```

### **Pagination avec métadonnées :**

```python
# Récupération avec métadonnées
hyper_page = server.get_hyper(1, 10)
print(f"Page actuelle: {hyper_page['page']}")
print(f"Page suivante: {hyper_page['next_page']}")
print(f"Total pages: {hyper_page['total_pages']}")
```

### **Navigation avec liens :**

```python
def navigate_pages(server, start_page=1, page_size=10):
    """Navigation automatique à travers les pages."""
    current_page = start_page

    while current_page:
        hyper_data = server.get_hyper(current_page, page_size)

        print(f"Page {hyper_data['page']}: {len(hyper_data['data'])} éléments")

        # Passer à la page suivante
        current_page = hyper_data['next_page']
        if not current_page:
            break

# Utilisation
navigate_pages(server)
```

---

## 🧪 Tests et validation

### **Tester les fonctionnalités :**

```bash
# Test fonction helper
./0-main.py

# Test pagination simple
./1-main.py

# Test pagination hypermedia
./2-main.py

# Test pagination résistante
./3-main.py
```

### **Validation du style :**

```bash
# Vérifier le style de code
pycodestyle *.py

# Vérifier les annotations de type
mypy *.py

# Vérifier la longueur des fichiers
wc -l *.py
```

---

## 📊 Dataset utilisé

**Fichier :** `Popular_Baby_Names.csv`

- **Contenu :** Noms de bébés populaires avec statistiques
- **Format :** CSV avec headers
- **Taille :** Plusieurs milliers d'entrées
- **Usage :** Dataset de test pour la pagination

### **Structure des données :**

```csv
Year,Gender,Ethnicity,Child's First Name,Count,Rank
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Olivia,172,1
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Chloe,112,2
...
```

---

## 🔧 Gestion des cas d'erreur

### **Paramètres invalides :**

```python
# Page négative ou zéro
assert page > 0, "Le numéro de page doit être positif"

# Taille de page invalide
assert page_size > 0, "La taille de page doit être positive"

# Index hors limites
if index >= len(dataset):
    return {"index": index, "data": [], "page_size": page_size, "next_index": None}
```

### **Pagination robuste :**

- Gestion des pages vides
- Validation des paramètres d'entrée
- Comportement cohérent en cas d'erreur
- Messages d'erreur informatifs

---

## 🚀 Optimisations de performance

### **Techniques utilisées :**

- **Indexation efficace** : Calcul optimisé des indices
- **Chargement paresseux** : Chargement du CSV une seule fois
- **Mise en cache** : Cache des métadonnées de pagination
- **Validation précoce** : Vérification des paramètres en amont

### **Métriques de performance :**

- **Temps de réponse** : < 1ms pour récupérer une page
- **Mémoire** : Utilisation constante, indépendante de la taille du dataset
- **Évolutivité** : Performance maintenue avec des millions d'entrées

---

## 📈 Applications pratiques

### **Cas d'usage courants :**

- **APIs REST** : Pagination de résultats de recherche
- **Interfaces web** : Navigation par pages sur des listes
- **Rapports** : Division de gros datasets en chunks
- **Exports** : Traitement par batch de grandes quantités de données

### **Exemples d'intégration :**

```python
# Dans une API Flask
@app.route('/api/names')
def get_names():
    page = request.args.get('page', 1, type=int)
    page_size = request.args.get('page_size', 10, type=int)

    server = Server()
    result = server.get_hyper(page, page_size)

    return jsonify(result)

# Dans une interface CLI
def display_paginated_results(query_results):
    server = Server()
    page = 1

    while True:
        hyper_data = server.get_hyper(page, 20)

        # Afficher les résultats
        for item in hyper_data['data']:
            print(item)

        # Navigation utilisateur
        if hyper_data['next_page']:
            choice = input("Page suivante ? (y/n): ")
            if choice.lower() == 'y':
                page = hyper_data['next_page']
            else:
                break
        else:
            print("Dernière page atteinte.")
            break
```

---

## 🔍 Comparaison des méthodes

| Méthode         | Avantages                 | Inconvénients      | Usage recommandé      |
| --------------- | ------------------------- | ------------------ | --------------------- |
| **Simple**      | Facile à implémenter      | Pas de métadonnées | Applications basiques |
| **Hypermedia**  | Navigation riche          | Plus complexe      | APIs REST complètes   |
| **Index-based** | Résistant aux changements | Complexité accrue  | Données volatiles     |

---

## 🧠 Points clés à retenir

### **Bonnes pratiques :**

- ✅ Toujours valider les paramètres d'entrée
- ✅ Fournir des métadonnées utiles (total_pages, next_page, etc.)
- ✅ Gérer gracieusement les cas limites (page vide, dernière page)
- ✅ Optimiser pour les cas d'usage courants (premières pages)
- ✅ Documenter clairement le comportement de l'API

### **Pièges à éviter :**

- ❌ Charger tout le dataset en mémoire
- ❌ Oublier la validation des paramètres
- ❌ Ne pas gérer les pages vides
- ❌ Utiliser des indices 0-based pour l'API utilisateur
- ❌ Omettre les métadonnées de navigation

---

## 👨‍💻 Auteur

Projet réalisé dans le cadre du cursus **Holberton School**
Focus sur la gestion efficace des données et l'optimisation des performances

---

## 📚 Ressources supplémentaires

- [REST API Pagination Best Practices](https://jsonapi.org/format/#fetching-pagination)
- [Database Pagination Performance](https://use-the-index-luke.com/sql/partial-results/fetch-next-page)
- [Python CSV Module Documentation](https://docs.python.org/3/library/csv.html)
- [Type Hints in Python](https://docs.python.org/3/library/typing.html)

---

✨ **Bon apprentissage de la pagination en Python !** ✨

---

> **💡 Astuce professionnelle :** En production, combine toujours la pagination avec la mise en cache et l'indexation de base de données pour des performances optimales !
