# Compte-rendu — semaine 1 (16 au 20 novembre 2026)

Date de la réunion : à compléter.

## Avant la réunion

### 1. Où j'en suis

Semaine 1 terminée, à l'heure sur le planning. Tous ses objectifs sont atteints,
et tous sont classés nécessaires.

### 2. Ce que j'ai compris

Un réseau bayésien décrit des causes et des effets par un graphe, avec une table
de probabilités par variable. Il permet de remonter d'un effet observé vers ses
causes probables, et de mettre à jour ces probabilités à chaque nouvelle
observation.

L'exemple de l'alarme le montre :

| Ce que l'on sait | Probabilité d'un cambriolage |
| --- | --- |
| Rien | 0,1 % |
| L'alarme sonne | 37 % |
| L'alarme sonne et la radio annonce un séisme | 0,3 % |

Deux leçons : un détecteur fiable d'un événement rare produit surtout de fausses alertes et une cause qui explique déjà un effet rend les autres causes moins probables (*explaining away*).

### 3. Ce que j'ai produit

- Le calcul de l'alarme à la main, rédigé dans le rapport :
  [`rapport/source/02_exemple_alarme.md`](../rapport/source/02_exemple_alarme.md).
- Le rapport Sphinx en place, avec un premier chapitre sur les bases :
  [`rapport/source/01_probabilites_et_factor_graphs.md`](../rapport/source/01_probabilites_et_factor_graphs.md).
- Le planning inversé avec priorisation : [`planning.md`](../planning.md).

### 4. Sources consultées

- Aide-mémoire CS221 sur les modèles à variables : utile comme référence, trop
  dense pour une première lecture.
- Vidéos Factor Graphs 1 et 2 : ont éclairci ce que l'aide-mémoire seul ne
  permettait pas de comprendre.
- Détail et commentaires : [`documentation/sources/`](../documentation/sources/).

### 5. Blocages, questions et suite

- Pas de blocage.
- Semaine 2 : représenter un réseau en Python et coder l'inférence exacte, avec
  des tests qui retrouvent les résultats de l'alarme.

## Après la réunion

### Échanges et décisions

- **Gibbs** : indispensable, le modèle doit fonctionner avec. Il passe en
  objectif nécessaire, semaine 3. Le planning a été réorganisé en conséquence,
  sans décaler la fin du nécessaire au-delà du 18 décembre.
- **Cas maternité** : le choix de la décision médicale est libre. Exemples
  retenus : « césarienne ou non », « traitement ou non », selon différents
  facteurs.
- **Données** : les données synthétiques sont acceptées. Pour les premiers
  prototypes, il vaut mieux des données dont on connaît les vraies probabilités.
- **Réunions** : la date de la réunion hebdomadaire est à mon choix.
- **Rendu** : début janvier.

### Actions pour la prochaine réunion

- [ ] Coder la représentation d'un réseau et l'inférence exacte
- [ ] Tests qui retrouvent les résultats de l'alarme
- [ ] Chapitre du rapport sur l'inférence exacte
- [ ] Poser la question de l'apprentissage de la structure
