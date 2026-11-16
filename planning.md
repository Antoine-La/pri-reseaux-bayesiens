# Planning inversé du PRI

Ébauche du 16 novembre 2026, à valider avec l'encadrant.

Le planning est construit à rebours depuis le rendu de début janvier. Les
objectifs nécessaires sont placés en premier et terminés le 18 décembre ; les
objectifs intéressants viennent ensuite ; les optionnels seulement s'il reste
du temps.

Rythme de travail : 4 heures par jour du lundi au vendredi, soit 20 heures par
semaine. Samedi et dimanche au repos.

## Priorisation des objectifs

| Priorité | Objectif | Semaine |
| --- | --- | --- |
| Nécessaire | Expliquer simplement un réseau bayésien, avec l'exemple de l'alarme calculé à la main | S1 |
| Nécessaire | Prototype : représenter un réseau et répondre à une question par inférence exacte | S2 |
| Nécessaire | Apprendre les probabilités conditionnelles à partir d'observations | S3 |
| Nécessaire | Appliquer le prototype au cas maternité, sur données synthétiques | S4 |
| Nécessaire | Mesurer l'erreur du modèle selon le nombre de patients | S5 |
| Nécessaire | Rapport pédagogique et dépôt GitHub public documenté | Continu, finalisé en S7 |
| Intéressant | Mesurer le temps d'entraînement et l'effet de la taille du réseau | S5 |
| Intéressant | Vérifier les résultats avec une bibliothèque spécialisée (pgmpy) | S4 |
| Intéressant | Inférence approchée par échantillonnage de Gibbs | S6 |
| Intéressant | Second exemple hors médical, pour montrer que la méthode se transpose | S7 |
| Optionnel | Apprendre avec des données manquantes (algorithme EM) | S8, si avance |
| Optionnel | Apprendre la structure du réseau, et pas seulement ses probabilités | S8, si avance |

Règle en cas de retard : on retire d'abord les objectifs optionnels, puis les
intéressants. Le nécessaire n'est jamais décalé au-delà du 18 décembre.

Point à valider : le classement de l'échantillonnage de Gibbs en « intéressant ».
L'encadrant l'a cité lors de la présentation du sujet.

## Jalons, en partant du rendu

| Échéance | Jalon | Ce qui doit être vrai à cette date |
| --- | --- | --- |
| Semaine du 4 janvier 2027 | Rendu et soutenance | Rapport, code et dépôt remis ; présentation répétée |
| 31 décembre | Rapport finalisé | Un lecteur non expert peut suivre le rapport du début à la fin |
| 24 décembre | Fin des objectifs intéressants | Gibbs codé et comparé au calcul exact, ou abandonné |
| 18 décembre | **Fin du nécessaire côté prototype** | Courbe d'erreur selon le nombre de patients obtenue |
| 11 décembre | Cas maternité | Le prototype répond à des questions d'aide à la décision |
| 4 décembre | Apprentissage | Le prototype retrouve les probabilités d'un réseau connu |
| 27 novembre | Inférence exacte | Le code redonne le résultat de l'alarme calculé à la main |
| 20 novembre | Fondations | Exemple de l'alarme résolu sur papier ; dépôt et rapport en place |

## Détail par semaine

### S1 · 16 au 20 novembre — Fondations (nécessaire)

- Objectif : savoir calculer à la main la probabilité d'une effraction sachant que l'alarme a sonné.
- À regarder : Factor Graphs 1 et 2 ; rappels de probabilités.
- À produire : dépôt GitHub public, squelette du rapport Sphinx, dossier de sources ; l'exemple de l'alarme résolu sur papier.

### S2 · 23 au 27 novembre — Réseau bayésien et inférence exacte (nécessaire)

- Objectif : représenter un réseau en Python et répondre à une question de façon exacte.
- À regarder : Bayesian Networks 1 – Inference.
- À produire : une classe de réseau, l'inférence par énumération, des tests vérifiés contre le calcul à la main.

### S3 · 30 novembre au 4 décembre — Apprentissage des probabilités (nécessaire)

- Objectif : retrouver les tables de probabilités d'un réseau à partir d'observations. C'est le cœur du sujet.
- À regarder : Bayesian Networks 3 – Maximum Likelihood.
- À produire : apprentissage par comptage (maximum de vraisemblance) et lissage de Laplace ; test sur un réseau connu.

### S4 · 7 au 11 décembre — Cas maternité (nécessaire)

- Objectif : appliquer le prototype au contexte de l'entreprise.
- À lire : sources sur l'aide à la décision en obstétrique, pour choisir des variables plausibles.
- À produire : un réseau d'une dizaine de variables, un générateur de patients synthétiques, des questions d'aide à la décision. Intéressant : vérification avec pgmpy.

### S5 · 14 au 18 décembre — Étude chiffrée (nécessaire, puis intéressant)

- Objectif : dire combien de patients il faut avant que l'outil soit fiable.
- À produire : la courbe d'erreur selon le nombre de patients. Intéressant : temps d'entraînement, effet de la taille du réseau.

### S6 · 21 au 24 décembre — Inférence approchée (intéressant, semaine allégée)

- Objectif : estimer une probabilité par échantillonnage quand le calcul exact devient trop coûteux.
- À regarder : Bayesian Networks 2 – Forward-Backward, partie sur l'échantillonnage de Gibbs.
- Si retard : cette semaine sert à finir le nécessaire, et Gibbs est abandonné.

### S7 · 28 au 31 décembre — Rapport pédagogique (nécessaire)

- Objectif : un lecteur non expert comprend le travail sans ambiguïté, peut le reproduire et l'appliquer ailleurs.
- À produire : rapport Sphinx finalisé, code nettoyé. Intéressant : un second exemple hors médical.

### S8 · 4 au 8 janvier — Rendu, soutenance et marge

- À produire : relecture, slides de soutenance, répétition chronométrée. Le temps restant absorbe les retards, ou sert aux objectifs optionnels.
