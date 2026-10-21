# Première installation et création du dépôt distant

## 1. Préparer les outils

- Git : vérifier dans PowerShell avec `git --version`.
- Python : vérifier avec `py -0p` (viser Python 3.12/3.13 pour le sprint de démarrage).
- VS Code : ouvrir le **dossier extrait**, pas seulement un fichier.

## 2. Créer le dépôt sur GitHub

1. Se connecter à GitHub puis ouvrir <https://github.com/new>.
2. Nom du dépôt : `hokodream-analytics` ; description depuis le README.
3. Visibilité : **Public**, pour le portfolio, **seulement après lecture des fichiers et vérification qu'aucune donnée sensible n'y figure**.
4. **Ne pas** cocher « Add a README », « Add .gitignore » ou « Choose a license » : ils sont traités localement (licence à décider plus tard).
5. Cliquer sur **Create repository**. Le dépôt sera alors vide.

## 3. Publier les fichiers depuis PowerShell

Après extraction du ZIP, ouvrir un terminal dans le dossier `hokodream-analytics` :

```powershell
git init
git branch -M main
git add .
git status
git commit -m "chore: initialize HOKODREAM Analytics project"
git remote add origin https://github.com/TON_PSEUDO_GITHUB/hokodream-analytics.git
git push -u origin main
```

**Remplace** `TON_PSEUDO_GITHUB` par ton identifiant GitHub. Vérifie bien `git status` **avant** `git commit` : aucun `.env`, token, export de compte réel ni donnée privée ne doit y figurer.

Si Git indique que ton nom et ton e-mail ne sont pas configurés :

```powershell
git config --global user.name "Ton nom GitHub"
git config --global user.email "adresse-utilisee-pour-les-commits@example.com"
```

Les exemples ci-dessus sont des *placeholders*, pas des valeurs à recopier telles quelles. GitHub peut demander une authentification via navigateur ; **n'envoie jamais ton mot de passe ni ton token à un assistant**.

## 4. Préparer l'environnement Python

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -e ".[dev]"
.\.venv\Scripts\python.exe -m pytest -q
```

Si tu utilises une autre version de Python, adapte la commande après vérification de compatibilité. L'environnement `.venv` est exclu par `.gitignore`.

## 5. Vérifier sur GitHub

- Le dépôt contient `README.md`, `docs/`, `src/`, `tests/`.
- Onglet **Actions** : le workflow « Python CI » exécute un test minimal. Il ne prouve pas que la collecte ni le dashboard fonctionnent.

## 6. Première mission réelle

Lire `docs/roadmap.md` puis commencer par confirmer le type de compte Instagram professionnel et valider les possibilités d'API avant de développer le collecteur.

### Dépannage

- `git : commande introuvable` : installer Git puis rouvrir PowerShell.
- `py -3.12` indisponible : utiliser `py -0p` pour voir les versions installées.
- `git push` échoue : vérifier l'URL exacte du dépôt, l'authentification et que le dépôt GitHub est vide.
- PowerShell bloque l'activation `.venv` : les commandes ci-dessus appellent directement Python et **ne nécessitent pas d'activer** l'environnement.
