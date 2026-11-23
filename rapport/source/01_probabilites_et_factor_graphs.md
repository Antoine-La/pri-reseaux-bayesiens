# Probabilités et factor graphs : les bases

Ce chapitre rassemble les notions nécessaires avant d'aborder les réseaux
bayésiens : trois outils de probabilités, puis les factor graphs, dont les
réseaux bayésiens sont un cas particulier.

## 1. Trois outils de probabilités

### La probabilité conditionnelle

$P(A \mid B)$ est la probabilité de $A$ une fois que l'on sait que $B$ est
vrai. Elle se lit « probabilité de $A$ sachant $B$ ».

$$
P(A \mid B) = \frac{P(A \cap B)}{P(B)}
$$

Savoir que $B$ est vrai réduit l'ensemble des possibles à $B$ ; on regarde
quelle part de $B$ est aussi dans $A$. Par exemple, avec un dé, la probabilité
d'obtenir 6 vaut 1/6. Si l'on sait que le résultat est pair, il ne reste que
2, 4 et 6, et la probabilité devient 1/3.

Attention : $P(A \mid B)$ et $P(B \mid A)$ sont deux nombres différents. La
probabilité d'avoir de la fièvre quand on a la grippe n'est pas celle d'avoir
la grippe quand on a de la fièvre.

### La règle de la chaîne

En retournant la définition, on obtient la probabilité que plusieurs
événements arrivent ensemble, en les prenant un par un :

$$
P(A, B, C) = P(A) \times P(B \mid A) \times P(C \mid A, B)
$$

C'est la règle qu'exploite un réseau bayésien : il décompose une probabilité
compliquée en un produit de petites probabilités conditionnelles.

### La formule de Bayes

Elle permet de remonter d'un effet observé vers sa cause, en retournant une
probabilité conditionnelle :

$$
P(A \mid B) = \frac{P(B \mid A)\, P(A)}{P(B)}
$$

| Terme | Nom | Sens |
| --- | --- | --- |
| $P(A)$ | probabilité a priori | ce que l'on croit avant d'observer |
| $P(B \mid A)$ | vraisemblance | à quel point l'observation est attendue si $A$ est vrai |
| $P(A \mid B)$ | probabilité a posteriori | ce que l'on croit après avoir observé $B$ |

Le dénominateur se calcule avec la formule des probabilités totales :
$P(B) = P(B \mid A)\, P(A) + P(B \mid \lnot A)\, P(\lnot A)$.

**Un exemple qui piège l'intuition.** Une maladie touche 1 % de la population.
Un test la détecte chez 90 % des malades, mais donne un faux positif chez 5 %
des personnes saines. Une personne testée positive n'a qu'environ **15 %** de
chances d'être malade :

$$
P(\text{malade} \mid \text{positif}) = \frac{0{,}90 \times 0{,}01}{0{,}90 \times 0{,}01 + 0{,}05 \times 0{,}99} \approx 0{,}154
$$

La maladie est rare, donc les faux positifs, nombreux parmi les 99 % de
personnes saines, l'emportent sur les vrais positifs. L'intuition se trompe
souvent sur ce type de question : c'est l'une des raisons d'être d'un outil
d'aide à la décision.

### L'indépendance

Deux événements sont **indépendants** quand connaître l'un ne change rien à la
probabilité de l'autre : $P(A \cap B) = P(A)\, P(B)$.

Ils peuvent aussi être **indépendants sachant** un troisième événement $C$ :
liés en général, ils ne le sont plus une fois $C$ connu.

$$
P(A \cap B \mid C) = P(A \mid C)\, P(B \mid C)
$$

Exemple : deux voisins appellent chacun quand ils entendent une alarme. Leurs
appels sont liés, car si l'un appelle, l'autre appellera probablement aussi.
Mais si l'on sait déjà que l'alarme sonne, l'appel de l'un n'apprend plus rien
sur celui de l'autre.

## 2. Les factor graphs

### L'idée

Au lieu de programmer la solution d'un problème, on le **décrit** : quelles
sont les inconnues, quelles valeurs elles peuvent prendre, et quelles
combinaisons sont bonnes ou mauvaises. Un algorithme générique cherche ensuite
les meilleures combinaisons. Cette description s'appelle un **factor graph**
(graphe de facteurs).

Exemple classique : colorier une carte en trois couleurs, sans que deux régions
voisines aient la même couleur.

### Le vocabulaire

| Notion | Définition |
| --- | --- |
| variable | une inconnue, avec son **domaine** : l'ensemble des valeurs possibles |
| affectation | un choix de valeur pour chaque variable |
| facteur | une fonction qui donne un score positif ou nul à une combinaison de valeurs ; 0 veut dire « interdit » |
| portée | les variables dont dépend un facteur |
| arité | le nombre de variables dans la portée : 1 pour un facteur unaire, 2 pour un binaire |
| poids d'une affectation | le **produit** de tous les facteurs |
| contrainte | un facteur qui ne vaut que 0 ou 1 |

$$
\text{Poids}(x) = \prod_{j} f_j(x)
$$

Comme c'est un produit, un seul facteur nul suffit à rendre le poids nul.

On dessine les variables en ronds et les facteurs en carrés, reliés aux
variables de leur portée.

### Trouver une bonne affectation

- **La recherche avec retour arrière** (*backtracking*) affecte les variables
  une à une et revient en arrière dès que le poids devient nul. Elle est exacte,
  mais son coût peut atteindre $|\text{domaine}|^n$ pour $n$ variables.
- **Des astuces l'accélèrent** : retirer au fur et à mesure les valeurs devenues
  impossibles chez les voisines (*forward checking*), traiter d'abord la variable
  la plus contrainte.
- **Des méthodes approchées** vont plus vite sans garantie : garder seulement
  les $K$ meilleures affectations partielles (*beam search*), ou partir d'une
  affectation complète et améliorer une variable à la fois (*ICM*).

### Exploiter l'indépendance

Le graphe montre directement quelles variables dépendent les unes des autres.

- Deux groupes de variables sans chemin entre eux sont **indépendants** : on
  les traite séparément, et les coûts s'additionnent au lieu de se multiplier.
- **Conditionner**, c'est fixer une variable à une valeur connue. On la retire
  du graphe, ce qui peut le couper en morceaux indépendants.
- Les voisines d'une variable forment sa **couverture de Markov** : si on les
  connaît, la variable devient indépendante de tout le reste.
- **Éliminer** une variable, c'est la faire disparaître en tenant compte de
  toutes ses valeurs : on multiplie les facteurs qui la contiennent, puis on
  prend le maximum (pour chercher la meilleure affectation) ou la somme (pour
  calculer des probabilités). On obtient un nouveau facteur sur ses voisines.
  L'ordre d'élimination compte : on commence par les variables qui ont peu de
  voisines.

## 3. Le lien avec les réseaux bayésiens

Un réseau bayésien est un factor graph particulier :

- chaque facteur est une **probabilité conditionnelle**, celle d'une variable
  sachant ses parents ;
- le poids d'une affectation devient sa **probabilité** ;
- éliminer des variables avec une **somme** permet de calculer exactement la
  probabilité de n'importe quel événement, sans énumérer toutes les situations.

Le chapitre suivant applique ces outils à l'exemple de l'alarme.

## Sources

- Stanford CS221, automne 2019, vidéos « Factor Graphs 1 » et « Factor Graphs 2 » :
  [playlist YouTube](https://www.youtube.com/playlist?list=PLoROMvodv4rO1NB9TD4iUZ3qghGEGtqNX).
- [Aide-mémoire CS221, modèles à variables](https://stanford.edu/~shervine/teaching/cs-221/cheatsheet-variables-models).
