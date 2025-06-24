# API Météo – Projet de fin de module

## 1. Objectifs

Ce projet a pour objectif de développer une plateforme complète permettant :
- d'interroger des données météorologiques en temps réel,
- de fournir des prévisions météo à partir de sources fiables (Open-Meteo),
- de visualiser les données via une interface Streamlit,
- de garantir la qualité logicielle à travers différents types de tests (unitaires, d'intégration, de contrat et de charge).

## 2. Architecture du projet

```
weather-api/
│
├── src/
│   ├── controllers/         # Contrôleurs FastAPI (endpoints)
│   ├── services/            # Logique de service (API externes)
│   ├── models/              # Modèles Pydantic
│   ├── tests/               # Tests unitaires, intégration, contrat
│
├── dashboard/               # Application Streamlit
│
├── config/                  # Fichiers de configuration
├── .env                     # Variables d’environnement
├── requirements.txt         # Dépendances du projet
├── docker-compose.yml       # Orchestration Docker
├── README.md                # Ce fichier
```

## 3. Fonctionnalités de l'API

- `GET /current/{city}` : Récupère les données météo actuelles pour une ville.
- `GET /forecast/{city}` : Récupère les prévisions météo à 7 jours.
- Gestion des erreurs personnalisée pour les villes inconnues ou erreurs d'API.

## 4. Interface utilisateur

L’interface est développée avec **Streamlit** et permet :
- de rechercher la météo actuelle d'une ville,
- d'afficher les prévisions à 7 jours,
- de visualiser les données sous forme de tableaux et graphiques.

## 5. Types de tests

| Type de test       | Objectif                                                      | Outils utilisés     |
|--------------------|---------------------------------------------------------------|---------------------|
| Tests unitaires     | Vérifier chaque fonction individuellement                     | `pytest`            |
| Tests d'intégration | Vérifier l’enchaînement logique entre les composants          | `pytest`, `respx`   |
| Tests de contrat    | Vérifier que l’API respecte son schéma attendu                | `schemathesis`      |
| Tests de charge     | Tester la performance sous un grand nombre de requêtes        | `locust`            |

Les tests sont automatisés via un conteneur Docker dédié, ou exécutables manuellement avec `pytest`.

## 6. Exécution du projet

### Lancer l’API :

```bash
uvicorn src.controllers.weather_controller:app --reload
```

### Lancer l’interface Streamlit :

```bash
streamlit run dashboard/app.py
```

### Lancer les tests manuellement :

```bash
pytest src/tests
```

### Lancer les tests de charge avec Locust :

```bash
locust -f locustfile.py
```

Puis ouvrir [http://localhost:8089](http://localhost:8089) dans un navigateur.

## 7. Dépendances

Toutes les dépendances sont listées dans `requirements.txt` :

```bash
pip install -r requirements.txt
```

### Exemples de bibliothèques utilisées :
- `fastapi`
- `httpx`
- `pytest`, `pytest-asyncio`
- `schemathesis`
- `streamlit`
- `locust`

## 8. Déploiement et conteneurisation

Même si chaque composant peut être lancé séparément, le projet propose aussi une orchestration via Docker Compose.

Exemple de conteneurs définis :
- `weather_api` : API FastAPI
- `weather_dashboard` : Interface Streamlit
- `weather_tests` : Tests automatiques à l'exécution
- `locust`  : Outil de test de charge

