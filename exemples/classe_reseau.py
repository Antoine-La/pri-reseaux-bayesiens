from itertools import product

class Reseau:
    def __init__(self):
        self.noms = []
        self.parents = {}
        self.tables = {}

    def ajouter_variable(self, nom, parents, tables):
        for parent in parents:
            if parent not in self.noms:
                raise ValueError(f"Le parent {parent} de {nom} n'a pas encore été ajouté")
        self.noms.append(nom)
        self.parents[nom] = parents
        self.tables[nom] = tables


    def proba_situation(self, situation):
        resultat = 1.0
        for nom in self.noms:
            # valeurs des parents de cette variable dans la situation,
            valeurs_parents = tuple(situation[p] for p in self.parents[nom])
            # P(nom = vrai | ses parents), lu dans la table
            p_vrai = self.tables[nom][valeurs_parents]
            # on multiplie par P(vrai) ou par P(faux) selon la valeur de la variable
            if situation[nom]:
                resultat = resultat * p_vrai
            else:
                resultat = resultat * (1 - p_vrai)
        return resultat


    def loi_jointe(self):

        jointe = {}
        for valeurs in product([True, False], repeat = len(self.noms)):
            situation = dict(zip(self.noms, valeurs))
            jointe[valeurs] = self.proba_situation(situation)
        return jointe


    def inference(self, requete, observations):

        loi_jointe = self.loi_jointe()
        totaux = {True: 0.0, False: 0.0}
        for valeurs, p in loi_jointe.items():
            situation = dict(zip(self.noms, valeurs))

            compatible = True
            for v, val in observations.items():
                if situation[v] != val:
                    compatible = False

            if compatible:
                valeur_requete = situation[requete]
                totaux[valeur_requete] += p

        somme = totaux[True] + totaux[False]
        if somme == 0:
            raise ValueError("Ces observations sont impossibles dans ce réseau")
        else:
            return {True: totaux[True] / somme, False: totaux[False] / somme}



if __name__ == "__main__":


    alarme = Reseau()
    alarme.ajouter_variable("C", [], {(): 0.001})
    alarme.ajouter_variable("S", [], {(): 0.002})
    alarme.ajouter_variable("A", ["C", "S"], {(True, True): 0.95, (True, False): 0.94,
                                              (False, True): 0.29, (False, False): 0.001})

    print("\n--- Alarme ---")
    print("P(A)          =", alarme.inference("A", {}))     
    print("P(C | A)      =", alarme.inference("C", {"A": True}))                # attendu : 0.3736
    print("P(C | A, S)   =", alarme.inference("C", {"A": True, "S": True}))     # attendu : 0.0033
    print("P(S | A)      =", alarme.inference("S", {"A": True}))        

    print("\n--- Pluie, bouchons, retard ---")
    trajet = Reseau()
    trajet.ajouter_variable("P", [], {(): 0.3})
    trajet.ajouter_variable("B", ["P"], {(True,): 0.8, (False,): 0.4})
    trajet.ajouter_variable("R", ["B"], {(True,): 0.5, (False,): 0.1})
    print("P(B)          =", trajet.inference("B", {}))                        
    print("P(R)          =", trajet.inference("R", {}))                         
    print("P(P | B)      =", trajet.inference("P", {"B": True}))                
    print("P(P | R)      =", trajet.inference("P", {"R": True}))        

    print("\n--- Maternité ---")
    maternite = Reseau()
    maternite.ajouter_variable("A", [], {(): 0.25})
    maternite.ajouter_variable("U", [], {(): 0.12})
    maternite.ajouter_variable("H", ["A"], {(True,): 0.10, (False,): 0.05})
    maternite.ajouter_variable("D", ["A"], {(True,): 0.20, (False,): 0.10})
    maternite.ajouter_variable("M", ["D"], {(True,): 0.20, (False,): 0.07})
    maternite.ajouter_variable("C", ["H", "M", "U"], {
        (True, True, True): 0.90,   (True, True, False): 0.70,
        (True, False, True): 0.80,  (True, False, False): 0.55,
        (False, True, True): 0.70,  (False, True, False): 0.35,
        (False, False, True): 0.50, (False, False, False): 0.12})    


    print("P(C)            =", maternite.inference("C", {}))                          # 0.211
    print("P(C | A)        =", maternite.inference("C", {"A": True}))                 # 0.228
    print("P(C | A, H)     =", maternite.inference("C", {"A": True, "H": True}))      # 0.594
    print("P(C | U)        =", maternite.inference("C", {"U": True}))                 # 0.535
    print("P(D | M)        =", maternite.inference("D", {"M": True}))                 # 0.290
    print("P(M | C)        =", maternite.inference("M", {"C": True}))                 # 0.169
    print("P(M | C, U)     =", maternite.inference("M", {"C": True, "U": True}))      # 0.115   


