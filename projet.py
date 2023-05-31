import ClassChamp
import datetime
import matplotlib.pyplot as plt


# création des classes contenues dans le fichier ClassChamp.py
Club = ClassChamp.Club
Joueur = ClassChamp.Joueur
Match = ClassChamp.Match
Championnat = ClassChamp.Championnat(Club)


# Modélisation des confrontations
Championnat.effectif()
                                        # importe les clubs et leurs joueurs
Championnat.generate_matches()          # On génère chacun des matchs entre ces différentes équipes, matchs allés d'abord puis match retours
Championnat.play_matches()              # On modélise le résultat de chacun de ces matchs et donc du championnat
Championnat.resultat()


# print(Championnat)                      # On affiche le resultat du championnat après le nombre de journées choisit
# print(Championnat.classement)         # C'est à dire le classement final


# Création du calendrier
debut_championnat = datetime.date(2023, 8, 6)  # Initialisation du début de championnat
nb_journees = 38
journees_par_semaine = 1
calendrier = ClassChamp.Calendrier(debut_championnat, nb_journees, journees_par_semaine, list(Championnat.clubs), Championnat) # Repartition des matchs selon les jours du calendrier



# print("Calendrier de la Ligue 1 :")         #Affichage du détail des différentes journées avec les résultats jours par jours
# for journee in range(1, nb_journees+1):
#     print("\nJournée {} ({}) :".format(journee, calendrier.get_date_journee(journee)))
#     calendrier.get_matchs_journee(journee)



Championnat.graphique_buts('Paris Saint-Germain')
Championnat.meilleurs_buteurs()
# print(Championnat.buts_encaisses())
# print(Championnat.vic_nul_def())
# print(calendrier.classement_journee(1))