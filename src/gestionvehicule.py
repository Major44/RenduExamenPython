""" Declaration de la classe Gestion Vehicules"""

from examenpython import ExamenPython

class GestionnaireVehicules:
    def __init__(self):
        self.vehicules = []

    def ajouter_vehicule(self, vehicule):
        self.vehicules.append(vehicule)
        print("Vehicule ajoute avec succes.")

    def supprimer_vehicule(self, immatriculation):
        vehicule_trouve = False
        for vehicule in self.vehicules:
            if vehicule.immatriculation == immatriculation:
                self.vehicules.remove(vehicule)
                vehicule_trouve = True
                break

        if vehicule_trouve:
            print("Vehicule supprime avec succes.")
        else:
            print("Aucun vehicule trouve avec cette immatriculation.")

    def modifier_vehicule(self, immatriculation, nouvelle_marque, nouveau_modele, nouvelle_annee, nouvelle_couleur):
        vehicule_trouve = False
        for vehicule in self.vehicules:
            if vehicule.immatriculation == immatriculation:
                vehicule.marque = nouvelle_marque
                vehicule.modele = nouveau_modele
                vehicule.annee = nouvelle_annee
                vehicule.couleur = nouvelle_couleur
                vehicule_trouve = True
                break

        if vehicule_trouve:
            print("Vehicule modifie avec succes.")
        else:
            print("Aucun vehicule trouve avec cette immatriculation.")

    def rechercher_vehicule(self, immatriculation):
        vehicule_trouve = False
        for vehicule in self.vehicules:
            if vehicule.immatriculation == immatriculation:
                print("Vehicule trouve :")
                print("Marque:", vehicule.marque)
                print("Modele:", vehicule.modele)
                print("Annee:", vehicule.annee)
                print("Couleur:", vehicule.couleur)
                print("Immatriculation:", vehicule.immatriculation)
                vehicule_trouve = True
                break

        if not vehicule_trouve:
            print("Aucun vehicule trouve avec cette immatriculation.")

    def afficher_vehicules(self):
        if len(self.vehicules) == 0:
            print("Aucun vehicule enregistre.")
        else:
            print("Liste des vehicules enregistres:")
            for i, vehicule in enumerate(self.vehicules):
                print("Vehicule", i + 1, ":")
                print("Marque:", vehicule.marque)
                print("Modele:", vehicule.modele)
                print("Annee:", vehicule.annee)
                print("Couleur:", vehicule.couleur)
                print("Immatriculation:", vehicule.immatriculation)
"""end"""