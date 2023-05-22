import ClassChamp
import datetime


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
Club= ClassChamp.Club
Joueur = ClassChamp.Joueur
Match = ClassChamp.Match
Championnat = ClassChamp.Championnat()


# Modélisation des confrontations
# On créer le championnat à l'aide de la liste Club et des class
Championnat.effectif()            # créées dans le fichier ClassChamp
Championnat.generate_matches()          # On génère chacun des matchs entre ces différentes équipes
Championnat.play_matches()              # On modélise le résultat de chacun de ces matchs

print(Championnat)                      # On affiche le resultat du championnat après le nombre de journées choisit
                                        # C'est à dire le classement


# Création des matchs et du calendrier


debut_championnat = datetime.date(2023, 8, 6)  # Initialisation du début de championnat
nb_journees = 38
journees_par_semaine = 1
calendrier = ClassChamp.Calendrier(debut_championnat, nb_journees, journees_par_semaine, list(Championnat.clubs), Championnat) # Initialisation du calendrier



print("Calendrier de la Ligue 1 :")         #Affichage du détail des différentes journées avec les résultats de tous
for journee in range(1, nb_journees+1):         # les matchs et les dates associées
    print("\nJournée {} ({}) :".format(journee, calendrier.get_date_journee(journee)))
    calendrier.get_matchs_journee(journee)

print(Championnat.graphique_buts)