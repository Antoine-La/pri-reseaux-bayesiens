# L'inférence exacte

Ce chapitre explique comment un programme répond à une question du type
« quelle est la probabilité d'une grippe, sachant que la personne tousse ? »,
pour n'importe quel petit réseau bayésien. La méthode est celle utilisée à la
main pour l'alarme au chapitre précédent ; elle est ici rendue automatique.

Le code complet est dans
[`exemples/classe_reseau.py`](https://github.com/Antoine-La/pri-reseaux-bayesiens/blob/main/exemples/classe_reseau.py).

## Le principe

**Inférence** : calculer la probabilité d'une variable que l'on ne voit pas
(la *requête*), à partir de variables que l'on a observées (les
*observations*). On la note $P(\text{requête} \mid \text{observations})$.

La méthode exacte la plus simple tient en trois étapes :

1. **Écrire la loi jointe** : la probabilité de chaque situation possible, par
   la règle de la chaîne.
2. **Garder les situations compatibles** avec les observations.
3. **Additionner et normaliser** : faire la somme de ces situations selon la
   valeur de la requête, puis diviser pour que le total fasse 1.

$$
P(Q = q \mid E = e) = \frac{\displaystyle\sum_{\text{situations où } Q = q \text{ et } E = e} P(\text{situation})}{\displaystyle\sum_{\text{situations où } E = e} P(\text{situation})}
$$

## L'exemple : un petit diagnostic

Quatre variables oui/non : $G$ (grippe), $L$ (allergie), $F$ (fièvre) et $T$
(toux). La grippe provoque fièvre et toux ; l'allergie provoque la toux.

```
Grippe (G)        Allergie (L)
   │    \              │
   ▼     \             │
Fièvre (F) \           │
            ▼          ▼
              Toux (T)
```

| Variable | Parents | $P(\text{vrai} \mid \text{parents})$ |
| --- | --- | --- |
| $G$ | aucun | 0,1 |
| $L$ | aucun | 0,2 |
| $F$ | $G$ | 0,8 si grippe, 0,05 sinon |
| $T$ | $G$, $L$ | 0,9 (grippe et allergie), 0,8 (grippe seule), 0,6 (allergie seule), 0,05 (aucune) |

La question : **une personne tousse ; quelle est la probabilité qu'elle ait la
grippe ?**

### Étape 1 : la loi jointe

Chaque situation est le produit d'une valeur lue dans chaque table :

$$
P(G, L, F, T) = P(G) \times P(L) \times P(F \mid G) \times P(T \mid G, L)
$$

Par exemple, pour « grippe, pas d'allergie, fièvre, toux » :
$0{,}1 \times 0{,}8 \times 0{,}8 \times 0{,}8 = 0{,}0512$. Avec 4 variables
oui/non, il y a $2^4 = 16$ situations, dont la somme vaut 1.

### Étape 2 : ne garder que les situations où la personne tousse

On élimine les 8 situations où $T$ est faux. Il en reste 8. La fièvre n'étant
pas observée, on garde les deux cas, avec et sans fièvre.

### Étape 3 : additionner et normaliser

On regroupe les 8 situations restantes selon la valeur de $G$ :

| Grippe ? | Somme des situations compatibles |
| --- | --- |
| oui | 0,082 |
| non | 0,144 |
| total | 0,226 |

$$
P(G \mid T) = \frac{0{,}082}{0{,}226} \approx 0{,}363
$$

**Quand une personne tousse, la probabilité d'une grippe passe de 10 % à
36 %.**

### D'autres questions, avec la même méthode

| Ce que l'on sait | Probabilité de grippe |
| --- | --- |
| Rien | 10 % |
| Elle tousse | 36 % |
| Elle tousse et a de la fièvre | 90 % |
| Elle tousse et elle est allergique | 14 % |

La dernière ligne montre l'*explaining away* déjà rencontré avec l'alarme :
l'allergie suffit à expliquer la toux, donc la grippe devient moins probable.

## La traduction en Python

Le programme représente un réseau par une classe `Reseau`. Chaque variable a un
nom, une liste de parents et une table. Comme les variables valent vrai ou faux,
une table ne stocke que $P(\text{vrai})$, pour chaque combinaison de valeurs
des parents :

```python
grippe = Reseau()
grippe.ajouter_variable("G", [], {(): 0.1})
grippe.ajouter_variable("L", [], {(): 0.2})
grippe.ajouter_variable("F", ["G"], {(True,): 0.8, (False,): 0.05})
grippe.ajouter_variable("T", ["G", "L"], {(True, True): 0.9, (True, False): 0.8,
                                          (False, True): 0.6, (False, False): 0.05})
```

Les trois étapes correspondent à trois méthodes :

| Méthode | Rôle |
| --- | --- |
| `proba_situation(situation)` | règle de la chaîne : probabilité d'une situation complète |
| `loi_jointe()` | appelle la précédente pour les $2^n$ situations possibles |
| `inference(requete, observations)` | étapes 2 et 3 : filtre, somme et normalisation |

La question de l'exemple s'écrit alors en une ligne :

```python
grippe.inference("G", {"T": True})     # {True: 0.363, False: 0.637}
```

## Vérification

Le même code, sans aucune modification, a été testé sur trois réseaux dont les
résultats avaient été calculés à la main :

| Réseau | Question | Calcul à la main | Programme |
| --- | --- | --- | --- |
| Diagnostic | $P(G \mid T)$ | 0,363 | 0,3628 |
| Diagnostic | $P(G \mid T, F)$ | 0,901 | 0,9011 |
| Alarme | $P(C \mid A)$ | 0,374 | 0,3736 |
| Alarme | $P(C \mid A, S)$ | 0,0033 | 0,0033 |
| Pluie, bouchons, retard | $P(\text{pluie} \mid \text{bouchons})$ | 0,46 | 0,4615 |

## Limite de la méthode

La loi jointe compte $2^n$ situations pour $n$ variables oui/non. C'est
instantané pour 6 variables (64 situations), lent vers 25 variables (plus de
30 millions) et impossible au-delà. Pour les réseaux plus grands, on utilise des
méthodes approchées, comme l'échantillonnage de Gibbs présenté au chapitre
suivant.
