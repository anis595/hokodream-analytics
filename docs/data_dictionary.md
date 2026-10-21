# Dictionnaire de données — à construire

Le schéma final n'est pas encore créé. Cette page sera complétée après la définition du contrat de données de démonstration.

Premiers champs candidats (non définitifs) :

| Champ | Type pressenti | Remarques |
|---|---|---|
| publication_id | texte | Identifiant stable et unique de publication |
| published_at | date/heure | Conserver le fuseau ou UTC |
| media_type | texte | Reel, photo, carrousel : valider les valeurs |
| measured_at | date/heure | Horodatage du relevé, pas de la publication |
| views | entier nullable | Seulement si la source fournit cette métrique |
| reach | entier nullable | Seulement si la source fournit cette métrique |
| source | texte | `demo`, `csv` ou `meta_api` |

**Ne jamais transformer une métrique indisponible en zéro : une absence n'est pas une performance nulle.**
