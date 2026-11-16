# Conventions Git du projet

## Branches

- `main` contient uniquement du travail terminé et relu. On n'y travaille pas
  directement.
- Une branche par semaine ou par sujet, nommée `sN-theme` :

| Branche | Contenu |
| --- | --- |
| `s1-fondations` | Probabilités, factor graphs, exemple de l'alarme |
| `s2-inference-exacte` | Classe de réseau, inférence par énumération |
| `s3-apprentissage` | Apprentissage des probabilités |
| `s4-cas-maternite` | Réseau maternité et données synthétiques |
| `s5-etude-chiffree` | Courbes d'erreur et de temps |
| `s6-gibbs` | Échantillonnage de Gibbs |
| `s7-rapport` | Finalisation du rapport |

- En fin de semaine, la branche est fusionnée dans `main` par une pull request
  sur GitHub, dont la description résume ce qui a été fait.
- Une correction rapide hors sujet de la semaine se fait sur une branche
  `correctif-description`.

## Messages de commit

Format : `type: description courte à l'infinitif`, en français, 70 caractères
au plus. Si besoin, une ligne vide puis une explication du pourquoi.

| Type | Usage | Exemple |
| --- | --- | --- |
| `code` | Ajout ou modification du prototype | `code: ajouter l'inférence par énumération` |
| `test` | Tests | `test: vérifier l'alarme contre le calcul à la main` |
| `docs` | Sources, journal, comptes-rendus, planning | `docs: commenter la vidéo Factor Graphs 1` |
| `rapport` | Pages du rapport Sphinx | `rapport: rédiger la page sur la formule de Bayes` |
| `exp` | Expériences et résultats | `exp: tracer l'erreur selon le nombre de patients` |
| `fix` | Correction d'une erreur | `fix: corriger la normalisation des tables` |

Règles :

- un commit par étape cohérente, pas un seul gros commit en fin de journée ;
- le message dit ce que le commit apporte, pas « mise à jour » ou « modifs » ;
- un push au minimum à chaque fin de séance.

## Formats de fichiers

Formats texte en priorité : Markdown (`.md`), Python (`.py`), reStructuredText
(`.rst`), CSV pour les données. Les fichiers binaires (Excel, Word, PDF) restent
hors du dépôt, sauf les figures produites par les expériences.
