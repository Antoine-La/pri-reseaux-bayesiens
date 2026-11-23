# L'exemple de l'alarme, calculé pas à pas

Cette page résout à la main le problème posé dans le sujet du projet. Le même
calcul est refait par le programme
[`exemples/alarme_verification.py`](https://github.com/Antoine-La/pri-reseaux-bayesiens/blob/main/exemples/alarme_verification.py),
qui retrouve exactement les mêmes résultats.

## Le problème

Une maison est équipée d'une alarme. Elle peut se déclencher pour deux raisons :
un **cambriolage**, ou un **tremblement de terre** qui fait vibrer les capteurs.
Elle n'est pas parfaite : elle peut rester muette pendant un cambriolage, ou
sonner sans raison.

Le sujet pose deux questions :

1. L'alarme sonne. Quelle est la probabilité d'un cambriolage ?
2. La radio annonce en plus un tremblement de terre. Que devient cette
   probabilité ?

## Les variables et le réseau

On utilise trois variables, chacune vraie ou fausse :

| Variable | Signification |
| --- | --- |
| $C$ | il y a un cambriolage |
| $S$ | il y a un séisme |
| $A$ | l'alarme sonne |

Le cambriolage et le séisme peuvent chacun déclencher l'alarme, et ils sont
indépendants l'un de l'autre. Le réseau a donc la forme d'un V :

```
Cambriolage (C)      Séisme (S)
          \             /
           ↘           ↙
            Alarme (A)
```

Les flèches vont de la cause vers l'effet.

## Les données

Les chiffres sont ceux de l'exemple classique du manuel de Russell et Norvig,
*Artificial Intelligence: A Modern Approach*.

| Donnée | Valeur | En mots |
| --- | --- | --- |
| $P(C)$ | 0,001 | un cambriolage une nuit sur 1 000 |
| $P(S)$ | 0,002 | un séisme une nuit sur 500 |
| $P(A \mid C, S)$ | 0,95 | cambriolage et séisme : l'alarme sonne 95 fois sur 100 |
| $P(A \mid C, \lnot S)$ | 0,94 | cambriolage seul : 94 fois sur 100 |
| $P(A \mid \lnot C, S)$ | 0,29 | séisme seul : 29 fois sur 100 |
| $P(A \mid \lnot C, \lnot S)$ | 0,001 | rien du tout : fausse alarme une nuit sur 1 000 |

Le symbole $\lnot$ se lit « non ». Six nombres suffisent : les autres s'en
déduisent, car une variable est soit vraie, soit fausse. Par exemple,
$P(\lnot A \mid C, S) = 1 - 0{,}95 = 0{,}05$.

## Étape 1 : la loi jointe

La **loi jointe** donne la probabilité de chacune des 8 situations possibles.
On l'obtient par la **règle de la chaîne**, simplifiée par le réseau : chaque
variable ne dépend que de ses parents.

$$
P(C, S, A) = P(C) \times P(S) \times P(A \mid C, S)
$$

Exemple pour la situation « cambriolage, pas de séisme, l'alarme sonne » :

$$
P(C, \lnot S, A) = 0{,}001 \times 0{,}998 \times 0{,}94 \approx 0{,}000\,938
$$

Les 8 situations :

| $C$ | $S$ | $A$ | Calcul | $P(C, S, A)$ |
| --- | --- | --- | --- | --- |
| V | V | V | 0,001 × 0,002 × 0,95 | 0,000 001 90 |
| V | V | F | 0,001 × 0,002 × 0,05 | 0,000 000 10 |
| V | F | V | 0,001 × 0,998 × 0,94 | 0,000 938 12 |
| V | F | F | 0,001 × 0,998 × 0,06 | 0,000 059 88 |
| F | V | V | 0,999 × 0,002 × 0,29 | 0,000 579 42 |
| F | V | F | 0,999 × 0,002 × 0,71 | 0,001 418 58 |
| F | F | V | 0,999 × 0,998 × 0,001 | 0,000 997 00 |
| F | F | F | 0,999 × 0,998 × 0,999 | 0,996 005 00 |

La somme des 8 lignes vaut 1. La dernière ligne, une nuit calme, pèse à elle
seule 99,6 %.

## Étape 2 : l'alarme sonne

On ne garde que les lignes où l'alarme sonne ($A$ = V) :

$$
P(A) = 0{,}000\,001\,90 + 0{,}000\,938\,12 + 0{,}000\,579\,42 + 0{,}000\,997\,00 \approx 0{,}002\,516
$$

Parmi elles, celles où il y a aussi un cambriolage :

$$
P(C, A) = 0{,}000\,001\,90 + 0{,}000\,938\,12 \approx 0{,}000\,940
$$

D'où, par la définition de la probabilité conditionnelle :

$$
P(C \mid A) = \frac{P(C, A)}{P(A)} = \frac{0{,}000\,940}{0{,}002\,516} \approx 0{,}374
$$

**Quand l'alarme sonne, la probabilité d'un cambriolage est d'environ 37 %.**

Ce résultat surprend, car l'alarme détecte 94 % des cambriolages. Mais les
cambriolages sont très rares, et les fausses alarmes, dues aux séismes ou à
rien du tout, sont au total plus fréquentes que les vraies : sur 1 000 nuits où
l'alarme sonne, environ 374 sont des cambriolages et 626 des fausses alertes.

## Étape 3 : la radio annonce un séisme

On ne garde plus que les lignes où l'alarme sonne **et** où il y a un séisme :

$$
P(C \mid A, S) = \frac{P(C, S, A)}{P(S, A)} = \frac{0{,}000\,001\,90}{0{,}000\,001\,90 + 0{,}000\,579\,42} \approx 0{,}003\,3
$$

**Si l'on apprend qu'il y a eu un séisme, la probabilité d'un cambriolage
retombe à environ 0,3 %.**

Le séisme suffit à expliquer l'alarme : on n'a plus besoin d'un cambriolage
pour la justifier. Pour comparaison, $P(S \mid A) \approx 0{,}231$ : quand
l'alarme sonne, il y a environ 23 % de chances qu'un séisme en soit la cause.

## Ce qu'il faut retenir

| Ce que l'on sait | Probabilité d'un cambriolage |
| --- | --- |
| Rien | 0,1 % |
| L'alarme sonne | 37 % |
| L'alarme sonne et il y a eu un séisme | 0,3 % |

Deux idées se dégagent :

- **La rareté compte autant que la fiabilité.** Un détecteur fiable d'un
  événement rare produit beaucoup de fausses alertes. C'est le même phénomène
  que pour un test de dépistage médical.
- **Une cause peut en « expliquer » une autre.** Le cambriolage et le séisme
  sont indépendants au départ. Mais dès que l'on observe l'alarme, ils
  deviennent liés : confirmer l'une des deux causes rend l'autre moins
  probable. On appelle ce phénomène l'*explaining away*. Il apparaît dès que
  deux flèches arrivent sur une même variable observée.

Un réseau bayésien fait ce raisonnement automatiquement : à chaque nouvelle
observation, il recalcule les probabilités de tout ce que l'on ne voit pas.
C'est ce que l'outil d'aide à la décision en maternité devra faire pour chaque
patiente.

## Limite du calcul à la main

Ici, 3 variables donnent 8 lignes. Avec 30 variables, la loi jointe en
compterait plus d'un milliard. C'est pourquoi la suite du projet utilise des
méthodes qui évitent d'écrire toute la loi jointe : l'élimination de variables
pour le calcul exact, et l'échantillonnage de Gibbs pour le calcul approché.
