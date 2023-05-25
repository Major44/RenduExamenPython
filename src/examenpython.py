"""Programme Principale """

from vehicule import Vehicule
from gestionvehicule import GestionnaireVehicules
from statistiquesvehicule import StatistiquesCirculation


class ExamenPython:
    def __init__(self):
        self.gestionnaire = GestionnaireVehicules()
        self.statistiques = StatistiquesCirculation(self.gestionnaire)

        vehicule1 = Vehicule ("BMW","C3",2018,"GRIS","BA144MD")
        vehicule2 = Vehicule ("RENAULT","SCENIC",2078,"JAUNE","BA144MD")
        vehicule3 = Vehicule ("ALPHA","D15",2028,"ROUGE","BA144MD")
        vehicule4 = Vehicule ("TESLA","M3",2020,"BLEU","BA144MD")
        vehicule5 = Vehicule ("AUDI","C3",2021,"ROSE","BA144MD")

        GestionnaireVehicules.ajouter_vehicule(vehicule1)
        GestionnaireVehicules.ajouter_vehicule(vehicule2)
        GestionnaireVehicules.ajouter_vehicule(vehicule3)
        GestionnaireVehicules.ajouter_vehicule(vehicule4)
        GestionnaireVehicules.ajouter_vehicule(vehicule5)

        GestionnaireVehicules.afficher_vehicules(vehicule4)
        GestionnaireVehicules.afficher_vehicules(vehicule5)

        GestionnaireVehicules.supprimer_vehicule(vehicule1)
        GestionnaireVehicules.modifier_vehicule(vehicule3)
        GestionnaireVehicules.modifier_vehicule(vehicule5)
      
    def execution(self):
        while True:
            print("\n=== Menu ===")
            print("1. Ajouter un vehicule")
            print("2. Supprimer un vehicule")
            print("3. Modifier un vehicule")
            print("4. Rechercher un vehicule")
            print("5. Afficher la liste des vehicules")
            print("6. Afficher les statistiques de circulation routiere")
            print("7. Quitter")

            choix = input("Votre choix : ")

            if choix == "1":
                marque = input("Marque: ")
                modele = input("Modele: ")
                annee = int(input("Annee: "))
                couleur = input("Couleur: ")
                immatriculation = input("Immatriculation: ")

                vehicule = Vehicule(marque, modele, annee, couleur, immatriculation)
                self.gestionnaire.ajouter_vehicule(vehicule)

            elif choix == "2":
                immatriculation = input("Entrez l'immatriculation du vehicule e supprimer: ")
                self.gestionnaire.supprimer_vehicule(immatriculation)

            elif choix == "3":
                immatriculation = input("Entrez l'immatriculation du vehicule e modifier: ")
                nouvelle_marque = input("Nouvelle marque: ")
                nouveau_modele = input("Nouveau modele: ")
                nouvelle_annee = int(input("Nouvelle annee: "))
                nouvelle_couleur = input("Nouvelle couleur: ")

                self.gestionnaire.modifier_vehicule(immatriculation, nouvelle_marque, nouveau_modele, nouvelle_annee, nouvelle_couleur)

            elif choix == "4":
                immatriculation = input("Entrez l'immatriculation du vehicule e rechercher: ")
                self.gestionnaire.rechercher_vehicule(immatriculation)

            elif choix == "5":
                self.gestionnaire.afficher_vehicules()

            elif choix == "6":
                self.statistiques.afficher_statistiques()

            elif choix == "7":
                print("Merci d'avoir utilise l'application. Au revoir !")
                break

            else:
                print("Choix invalide. Veuillez reessayer.")



main = ExamenPython()
main.execution()   
"""execution de la fonction main"""
"""end"""