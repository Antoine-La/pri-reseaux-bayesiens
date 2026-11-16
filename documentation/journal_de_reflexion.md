# Journal de réflexion

Les questions que je me pose, les réponses partielles, les choix faits et les
pistes abandonnées, datés. Entrée la plus récente en haut.

## Questions ouvertes

| Depuis le | Question | Réponse partielle | État |
| --- | --- | --- | --- |
| 2026-11-14 | Quelle est la date du rendu et de la soutenance ? | Début janvier ; planning calé sur la semaine du 4 janvier | À poser à l'encadrant |
| 2026-11-14 | Quel jour a lieu la réunion hebdomadaire ? | | À poser à l'encadrant |
| 2026-11-14 | Quelle décision médicale précise le cas maternité doit-il éclairer ? | | À poser à l'encadrant |
| 2026-11-14 | Des données synthétiques sont-elles acceptables pour le prototype ? | Hypothèse retenue : oui, faute de données réelles | À poser à l'encadrant |
| 2026-11-14 | Faut-il apprendre la structure du réseau, ou seulement ses probabilités ? | Le sujet parle des probabilités conditionnelles ; structure classée optionnelle | À poser à l'encadrant |
| 2026-11-16 | L'échantillonnage de Gibbs est-il nécessaire ou seulement intéressant ? | Classé intéressant : le prototype fonctionne avec l'inférence exacte sur un petit réseau | À poser à l'encadrant |

## 2026-11-16 — Mise en conformité avec les consignes du PRI

- **Décision** : le planning devient un planning inversé avec priorisation
  (nécessaire, intéressant, optionnel), voir `planning.md`.
- **Décision** : l'apprentissage des probabilités passe en semaine 3, avant
  l'échantillonnage de Gibbs, pour que tout le nécessaire soit terminé le
  18 décembre.
- **Décision** : les sources sont rangées par thème dans `documentation/sources/`,
  avec un commentaire d'utilité par ressource.
- **Décision** : dépôt rendu public, une branche par semaine, messages de commit
  normalisés, voir `documentation/conventions_git.md`.
- **Décision** : rythme d'entreprise, 4 heures par jour du lundi au vendredi.

## 2026-11-14 — Cadrage du projet

- **Décision** : coder le cœur du prototype à la main pour pouvoir l'expliquer,
  puis vérifier les résultats avec une bibliothèque spécialisée (pgmpy).
- **Décision** : données synthétiques uniquement ; le générateur de patients
  fait partie du livrable.
- **Décision** : rapport rédigé avec Sphinx, une page par thème, écrite la
  semaine où le thème est traité.
