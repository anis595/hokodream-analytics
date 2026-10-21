# Roadmap — HOKODREAM Analytics

Rythme prévu : **1 h du lundi au jeudi + 3 h le vendredi, samedi et dimanche = 13 h/semaine**. Les durées sont des estimations, non des garanties.

## Jalons indicatifs

| Période | Objectif démontrable |
|---|---|
| Semaines 1–2 | Structure GitHub, faisabilité API évaluée, contrat des données de démo |
| Semaines 3–4 | Jeu de données synthétiques + première ingestion et vérifications |
| Semaines 5–6 | Schéma PostgreSQL, requêtes SQL, premier dashboard |
| Semaines 7–8 | Amélioration des KPI, automatisation **si accès disponibles**, tests |
| Semaines 9–10 | Power BI Desktop, documentations, démonstration et marges |

Les jalons bougeront selon l'apprentissage. **La voie `demo` fonctionne même si Meta bloque**. Le travail sur une API réelle ne doit pas empêcher le MVP de devenir présentable.

## Sprint 1 — une seule tâche active à la fois

- [ ] **HKA-001 — Proof of Access Instagram** : confirmer Business/Créateur ; lire la documentation et déterminer les permissions utiles ; tester une authentification autorisée ; noter les métriques réellement accessibles ou le blocage précis. Aucun token dans le GitHub.
- [ ] **HKA-002 — GitHub** : dépôt public créé, README affiché, CI initiale verte.
- [ ] **HKA-003 — Contrat de données de démo** : définir champs `publication_id`, `date_publication`, `type_media`, `date_mesure`, métriques (avec null possibles), provenance et règles de contrôle.
- [ ] **HKA-004 — Générateur de démo** : produire des données **synthétiques**, reproductibles avec seed documentée, sans simuler des résultats réels.

### Critères pour considérer le Sprint 1 terminé

Le dépôt distant existe ; aucun secret n'est versionné ; on peut exécuter le test initial ; les possibilités de l'API sont décrites **sans les supposer acquises** ; la prochaine source de données est définie.

## Règles de fonctionnement

1. Une seule tâche active à la fois.
2. Chaque nouvelle fonctionnalité commence par la question métier qu'elle sert.
3. Les tests doivent prouver la fonctionnalité livrée, pas seulement que Python importe un module.
4. Avant de publier un jeu de données, vérifier la confidentialité et la provenance.
5. Pas de nouveaux frameworks sans besoin réel.
