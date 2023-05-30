import ClassChamp
import datetime
import matplotlib.pyplot as plt

''' A FAIRE:
- héritage entre les classes, chiant il va falloir modifier des trucs
- héritage depuis un type déjà existant, genre List
- commentaires
- tests : au moins 4 méthodes avec 2 cas par méthode

- Vérifier que si un club remporte un match, alors il a marqué plus de buts que l’adversaire
- Vérifier que le nombre de points distribués lors d’une journée est compris entre 2 et 3 fois le nombre de matchs
- Vérifier que le nombre de matchs joués par journée est égal au nombre de clubs/2
- Sauvegarde : Votre modèle de championnat devra pouvoir être sauvé et relu depuis un fichier
- Choix d’une journée particulière : scores, notes des joueurs, etc
- Choix d’une journée pour le championnat en cours : classement des clubs, nombre de matchs gagnés/nuls/perdus par club, nombre de buts marqués/encaissés par club
- faire des analyses sur les stats des clubs ou joueurs
'''

#création des classes contenues dans le fichier ClassChamp.py
Club = ClassChamp.Club
Joueur = ClassChamp.Joueur
Match = ClassChamp.Match
Championnat = ClassChamp.Championnat()


# Modélisation des confrontations
Championnat.effectif()
                                        # importe les clubs et leurs joueurs
Championnat.generate_matches()          # On génère chacun des matchs entre ces différentes équipes, matchs allés d'abord puis match retours
Championnat.play_matches()              # On modélise le résultat de chacun de ces matchs et donc du championnat
Championnat.resultat()

# print(Championnat)                      # On affiche le resultat du championnat après le nombre de journées choisit
# print(Championnat.resultat())                        # C'est à dire le classement final
print(Championnat.buts_marque())

# Création du calendrier
debut_championnat = datetime.date(2023, 8, 6)  # Initialisation du début de championnat
nb_journees = 38
journees_par_semaine = 1
calendrier = ClassChamp.Calendrier(debut_championnat, nb_journees, journees_par_semaine, list(Championnat.clubs), Championnat) # Repartition des matchs selon les jours du calendrier



# print("Calendrier de la Ligue 1 :")         #Affichage du détail des différentes journées avec les résultats jours par jours
# for journee in range(1, nb_journees+1):
#     print("\nJournée {} ({}) :".format(journee, calendrier.get_date_journee(journee)))
#     calendrier.get_matchs_journee(journee)

# print(Championnat.graphique_buts)