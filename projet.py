import ClassChamp
import datetime

Club= ClassChamp.Club()
Joueur = ClassChamp.Joueur()
Match = ClassChamp.Match()

psg = Club("Paris Saint-Germain")
om = Club("Olympique de Marseille")
asm = Club("AS Monaco")
ol = Club("Olympique Lyonnais")
losc = Club("Lille OSC")


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
calendrier = ClassChamp.()
calendrier.add_match(Match(psg, om, datetime.date(2023, 4, 8)))
calendrier.add_match(Match(asm, ol, datetime.date(2023, 4, 9)))
calendrier.add_match(Match(psg, asm, datetime.date(2023, 4, 15)))
calendrier.add_match(Match(ol, losc, datetime.date(2023, 4, 16)))
calendrier.add_match(Match(om, losc, datetime.date(2023, 4, 22)))

# Modélisation des confrontations
for match in calendrier.get_journee(1):
    resultat = match.jouer_match()
    print(f"{match.home_team.name} {resultat[0]} - {resultat[1]} {match.away_team.name}")

# Résultat :
# Paris Saint-Germain 2 - 1 Olympique de Marseille
# AS Monaco 1 - 0 Olympique Lyonnais

for match in calendrier.get_journee(2):
    resultat = match.jouer_match()
    print(f"{match.home_team.name} {resultat[0]} - {resultat[1]} {match.away_team.name}")

# Résultat :
# Paris Saint-Germain 3 - 2 AS Monaco
# Olympique Lyonnais 1 - 1 Lille OSC

for match in calendrier.get_journee(3):
    resultat = match.jouer_match()
    print(f"{match.home_team.name} {resultat[0]} - {resultat[1]} {match.away_team.name}")

# Résultat :
# Olympique de Marseille 2 - 2 Lille OSC
