# HOKODREAM Analytics

> **Projet fil rouge Data Analyst** — Python · SQL · PostgreSQL · Streamlit · Power BI

**FR** — Construction progressive d'un pipeline d'analyse des performances de contenus Instagram pour HOKODREAM (vidéo / drone FPV), avec une version de démonstration indépendante des autorisations Meta.

**EN** — An evolving data analytics portfolio project: ingest, validate, transform, store and visualize social media performance data. Includes a synthetic-data demo path independent of Instagram API access.

## Statut réel du projet

**Sprint 1 — Initialisation.** Le dépôt contient la structure, le cahier des charges et un test de vérification de l'installation. **Il ne contient pas encore de collecteur Instagram, de base PostgreSQL, de pipeline analytique ni de dashboard fonctionnel.** Ces éléments seront développés et testés progressivement.

## Problème métier

Quels types de contenus HOKODREAM produisent de l'engagement ? Comment comparer les Reels, photos et autres publications sans interpréter à tort des métriques incomplètes ou des publications d'âges différents ?

Les métriques accessibles seront confirmées **après** un premier test avec l'API officielle. Les données de démonstration seront toujours identifiées comme synthétiques.

## Architecture cible

```text
Instagram (si API autorisée) ─┐
                              ├─> Collecte Python ─> Qualité / transformations ─> PostgreSQL
Données démo / CSV ───────────┘                                           │
                                                                         ├─> SQL / KPI
                                                                         ├─> Streamlit
                                                                         └─> Power BI Desktop
```

Cette architecture est une **cible**, pas une fonctionnalité déjà livrée.

## Démarrage sur Windows

Prérequis : **Git**, **Python 3.12 ou 3.13** (version recommandée à vérifier avec la formation), **VS Code**. PostgreSQL sera installé lorsqu'on abordera la base de données.

```powershell
cd hokodream-analytics
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -e ".[dev]"
.\.venv\Scripts\python.exe -m pytest
```

Si `py -3.12` n'est pas disponible, vérifie la version installée avec `py -0p`, puis adapte la commande. Le premier test ne valide que la structure et l'import du package, **pas** le traitement de données.

Voir [`docs/INSTALLATION_WINDOWS.md`](docs/INSTALLATION_WINDOWS.md) pour publier le dépôt sur GitHub et les commandes exactes.

## Documentation

- [Cahier des charges détaillé](docs/cahier_des_charges.md)
- [Roadmap et première mission](docs/roadmap.md)
- [Architecture et limites](docs/architecture.md)
- [Décisions et risques](docs/decisions.md)
- [Dictionnaire de données](docs/data_dictionary.md) (à compléter)
- [Définitions KPI](docs/kpi_definitions.md) (à compléter)

## Environnement, coût et sécurité

- Objectif de démarrage : **0 € de dépenses supplémentaires**.
- Aucun token, mot de passe, fichier `.env` réel ou donnée sensible ne doit être versionné.
- Seules des données synthétiques et autorisées seront rendues publiques.
- Accès API Meta : **non encore validé**. Les fonctionnalités Instagram sont conditionnelles.
- Démonstration Streamlit et rapport Power BI : **non encore développés**.
- Ce dépôt n'inclut pas de licence open source pour le moment : le choix sera fait explicitement avant toute réutilisation par des tiers.

## Objectif portfolio

Présenter une démarche complète : question métier, sources et qualité de données, Python / pandas, modélisation SQL, visualisations, interprétation, tests et limites. **Comprendre et pouvoir défendre tous les choix techniques.**
