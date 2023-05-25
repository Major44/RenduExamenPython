""" Declaration de la classe Statistiques Vehicules"""

class StatistiquesCirculation:
    def __init__(self, gestionnaire_vehicules):
        self.gestionnaire_vehicules = gestionnaire_vehicules

    def afficher_statistiques(self):
        nb_voitures_rouges = 0
        nb_motos = 0

        for vehicule in self.gestionnaire_vehicules.vehicules:
            if vehicule.couleur == "rouge":
                nb_voitures_rouges += 1

        print("Statistiques de circulation routiere :")
        print("Nombre de voitures rouges :", nb_voitures_rouges)
"""end"""