import ClassChamp
import datetime

Club= ClassChamp.Club
Joueur = ClassChamp.Joueur
Match = ClassChamp.Match
Championnat = ClassChamp.Championnat()

psg = Club("Paris Saint-Germain","Paris")
om = Club("Olympique de Marseille","Marseille")
asm = Club("AS Monaco","Monaco")
ol = Club("Olympique Lyonnais","Lyon")
losc = Club("Lille OSC","Lyon")


# Création des joueurs pour chaque club
psg.add_player(Joueur("Kylian Mbappé", 10))
psg.add_player(Joueur("Neymar", 9))
om.add_player(Joueur("Dimitri Payet", 6))
om.add_player(Joueur("Florian Thauvin", 7))
asm.add_player(Joueur("Wissam Ben Yedder", 8))
asm.add_player(Joueur("Kevin Volland", 7))
ol.add_player(Joueur("Memphis Depay", 11))
ol.add_player(Joueur("Lucas Paqueta", 6))
losc.add_player(Joueur("Jonathan David", 8))
losc.add_player(Joueur("Burak Yilmaz", 10))




# Création des matchs et du calendrier




debut_championnat = datetime.date(2023, 8, 6)
nb_journees = 38
journees_par_semaine = 1
Equipe = ["PSG", "OM", "OL", "ASM", "LOSC", "ASSE", "FCN", "RCL", "OGCN", "FCM"]
calendrier = ClassChamp.Calendrier(debut_championnat, nb_journees, journees_par_semaine, Equipe)
calendrier.calculer_calendrier()



# Modélisation des confrontationsé
for i in Equipe:
    Championnat.add_club(i)
Championnat.generate_matches()
Championnat.play_matches()

print(Championnat)


print("Calendrier de la Ligue 1 :")
for journee in range(1, nb_journees+1):
    print("Journée {} ({}) :".format(journee, calendrier.get_date_journee(journee)))
    matchs_journee = calendrier.get_matchs_journee(journee)
    for match in matchs_journee:
        print(match)