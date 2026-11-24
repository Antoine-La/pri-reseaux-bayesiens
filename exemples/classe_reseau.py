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
            # valeurs des parents de cette variable dans la situation
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
        # boucle sur toutes les situations possibles,
        # renvoie le dictionnaire situation -> probabilité
        ...

    def inference(self, requete, observations):
        # (demain) additionner les lignes de la loi jointe
        # compatibles avec les observations, puis normaliser
        ...


if __name__ == "__main__":

    grippe = Reseau()
    grippe.ajouter_variable("G", [], {(): 0.1})
    grippe.ajouter_variable("L", [], {(): 0.2})
    grippe.ajouter_variable("F", ["G"], {(True,): 0.8, (False,): 0.05})
    grippe.ajouter_variable("T", ["G", "L"], {(True, True): 0.9, (True, False): 0.8,
                                              (False, True): 0.6, (False, False): 0.05})

    # Test de la règle de la chaîne 
    situation = {"G": True, "L": False, "F": True, "T": True}
    print("P(grippe, pas d'allergie, fièvre, toux) =", grippe.proba_situation(situation))
