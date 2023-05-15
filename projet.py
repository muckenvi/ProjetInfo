import ClassChamp
import datetime



Club= ClassChamp.Club
Joueur = ClassChamp.Joueur
Match = ClassChamp.Match
Championnat = ClassChamp.Championnat()

# Création des clubs
''''

Ajaccio=Club('AC Ajaccio','Ajaccio')
Ajaccio.effectif()
Angers=Club('SCO Angers','Angers')
Angers.effectif()
Auxerre=Club('AJ Auxerre','Auxerre')
Auxerre.effectif()
Brest=Club('Stade Brestois 29','Brest')
Brest.effectif()
Clermont=Club('Clermont Foot 63','Clermont')
Clermont.effectif()
Lens=Club('RC Lens','Lens')
Lens.effectif()
Lille=Club('Lille OSC','Lille')
Lille.effectif()
Lorient=Club('FC Lorient','Lorient')
Lorient.effectif()
Lyon=Club('Olympique Lyonnais','Lyon')
Lyon.effectif()
Marseille=Club('Olympique de Marseille','Marseille')
Marseille.effectif()
Monaco=Club('AS Monaco','Monaco')
Monaco.effectif()
Montpellier=Club('Montpellier HSC','Montpellier')
Montpellier.effectif()
Nantes=Club('FC Nantes','Nantes')
Nantes.effectif()
Nice=Club('OGC Nice','Nice')
Nice.effectif()
Paris=Club('Paris Saint-Germain','Paris')
Paris.effectif()
Reims=Club('Stade de Reims','Reims')
Reims.effectif()
Rennes=Club('Stade Rennais FC','Rennes')
Rennes.effectif()
Strasbourg=Club('RC Strasbourg Alsace','Strasbourg')
Strasbourg.effectif()
Toulouse=Club('Toulouse FC','Toulouse')
Toulouse.effectif()
Troyes=Club('ES Troyes AC','Troyes')
Troyes.effectif()

# Liste regroupant les différentes équipes de ligue 1
Clubs = [Ajaccio, Angers, Auxerre, Brest, Clermont, Lens, Lille, Lorient, Lyon, Marseille,
           Monaco, Montpellier, Nantes, Nice, Paris, Reims, Rennes, Strasbourg, Toulouse, Troyes]

'''


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