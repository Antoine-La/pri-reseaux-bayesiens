# PRI — Réseaux bayésiens pour la modélisation du risque

Projet de recherche individuel (INSA), de novembre 2026 à janvier 2027.

## Objectif

Découvrir les réseaux bayésiens, puis construire un prototype Python qui apprend
les probabilités conditionnelles d'un réseau à partir d'observations.

Cas d'application : une aide probabiliste à la décision médicale en maternité,
pour une PME qui vend du matériel médical à des hôpitaux. Les données utilisées
sont synthétiques : aucune donnée patient réelle, aucune valeur clinique.

## Par où commencer

| Je cherche | Fichier |
| --- | --- |
| Le planning inversé et la priorisation des objectifs | [`planning.md`](planning.md) |
| Les ressources consultées et leur utilité | [`documentation/sources/`](documentation/sources/) |
| Les questions, réponses partielles et choix faits | [`documentation/journal_de_reflexion.md`](documentation/journal_de_reflexion.md) |
| Ce qui a été présenté et dit en réunion | [`comptes_rendus/`](comptes_rendus/) |
| Le code du prototype | [`src/reseau_bayesien/`](src/reseau_bayesien/) |

Les dossiers des tests, des expériences et du rapport Sphinx seront ajoutés au
fil du projet, quand ils auront du contenu.

## Avancement

| Semaine | Thème | Priorité | État |
| --- | --- | --- | --- |
| S1 · 16 au 20 nov. | Fondations : probabilités, factor graphs, exemple de l'alarme | Nécessaire | En cours |
| S2 · 23 au 27 nov. | Réseau bayésien et inférence exacte | Nécessaire | À faire |
| S3 · 30 nov. au 4 déc. | Apprentissage des probabilités | Nécessaire | À faire |
| S4 · 7 au 11 déc. | Cas maternité | Nécessaire | À faire |
| S5 · 14 au 18 déc. | Étude chiffrée : erreur et temps selon le volume de données | Nécessaire, puis intéressant | À faire |
| S6 · 21 au 24 déc. | Inférence approchée (échantillonnage de Gibbs) | Intéressant | À faire |
| S7 · 28 au 31 déc. | Rapport pédagogique Sphinx | Nécessaire | À faire |
| S8 · 4 au 8 janv. | Rendu, soutenance et marge | Nécessaire | À faire |

Les dates supposent un rendu la semaine du 4 janvier 2027 (à confirmer).

## Organisation du travail avec Git

- Une branche par semaine (par exemple `Semaine-1---Fondation`), fusionnée dans
  `main` en fin de semaine par une pull request qui résume la semaine.
- Un commit par séance de travail au minimum, avec un message qui dit ce qui a
  avancé.
- Fichiers en formats texte (Markdown, Python) pour que chaque modification soit
  suivie ; les documents bureautiques restent hors du dépôt.
