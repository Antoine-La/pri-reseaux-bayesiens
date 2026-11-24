# Vérification du calcul de l'alarme (semaine 1)
# Réseau : Cambriolage -> Alarme <- Seisme
# Chiffres de l'exemple de Russell et Norvig.

from itertools import product

p_cambriolage = 0.001
p_seisme = 0.002
# P(alarme | cambriolage, seisme)
p_alarme = {(True, True): 0.95, (True, False): 0.94,
            (False, True): 0.29, (False, False): 0.001}


def p(proba_vrai, valeur):
    return proba_vrai if valeur else 1 - proba_vrai


# Loi jointe par la règle de la chaîne : P(C, S, A) = P(C) P(S) P(A | C, S)
jointe = {}
for c, s, a in product([True, False], repeat=3):
    jointe[(c, s, a)] = p(p_cambriolage, c) * p(p_seisme, s) * p(p_alarme[(c, s)], a)

print("Somme des 8 cas :", round(sum(jointe.values()), 6))

# P(C | A)
p_a = sum(v for (c, s, a), v in jointe.items() if a)
p_c_et_a = sum(v for (c, s, a), v in jointe.items() if c and a)
print("P(C | A)    =", round(p_c_et_a / p_a, 4)*100,"%")      # attendu : 0.374

# P(C | A, S)
p_a_s = sum(v for (c, s, a), v in jointe.items() if a and s)
p_c_a_s = jointe[(True, True, True)]
print("P(C | A, S) =", round(p_c_a_s / p_a_s, 4)*100,"%")     # attendu : 0.0033
