# PRI — Réseaux bayésiens pour la modélisation du risque

Projet de recherche individuel (INSA), de novembre 2026 à janvier 2027.

## Objectif

Découvrir les réseaux bayésiens, puis construire un prototype Python qui apprend
les probabilités conditionnelles d'un réseau à partir d'observations.

Cas d'application : une aide probabiliste à la décision médicale en maternité,
pour une PME qui vend du matériel médical à des hôpitaux. Les données utilisées
sont synthétiques : aucune donnée patient réelle, aucune valeur clinique.

## Organisation du dépôt

| Dossier | Contenu |
| --- | --- |
| `src/reseau_bayesien/` | Code du prototype (réseau, inférence, apprentissage) |
| `tests/` | Tests du code |
| `experiences/` | Scripts et résultats de l'étude chiffrée |
| `rapport/` | Rapport-formation généré avec Sphinx |
| `documentation/` | Journal des sources et journal de réflexion |
| `comptes_rendus/` | Un compte-rendu par réunion hebdomadaire |

## Avancement

| Semaine | Thème | État |
| --- | --- | --- |
| S1 · 16 au 22 nov. | Fondations : probabilités, factor graphs, exemple de l'alarme | À faire |
| S2 · 23 au 29 nov. | Réseau bayésien et inférence exacte | À faire |
| S3 · 30 nov. au 6 déc. | Inférence approchée (échantillonnage de Gibbs) | À faire |
| S4 · 7 au 13 déc. | Apprentissage des probabilités | À faire |
| S5 · 14 au 20 déc. | Cas maternité | À faire |
| S6 · 21 au 27 déc. | Étude chiffrée : erreur et temps selon le volume de données | À faire |
| S7 · 28 déc. au 3 janv. | Rapport-formation Sphinx | À faire |
| S8 · 4 au 10 janv. | Soutenance et marge | À faire |

Les dates supposent une soutenance la semaine du 4 janvier 2027 (à confirmer).

## Source de départ

Cours Stanford CS221 (automne 2019), vidéos Factor Graphs 1 et 2 et Bayesian
Networks 1, 2 et 3 :
https://www.youtube.com/playlist?list=PLoROMvodv4rO1NB9TD4iUZ3qghGEGtqNX
