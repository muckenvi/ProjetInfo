Ce fichier est à lire pour bien comprendre comment utiliser les fichiers projet.py et ClassChamp.py

Pour lancer le code il faut taper les lignes suivantes:
import ClassChamp
Club = ClassChamp.Club
Joueur = ClassChamp.Joueur
Match = ClassChamp.Match
Championnat = ClassChamp.Championnat(Club)
Championnat.effectif()              # importe les clubs et leurs joueurs
Championnat.generate_matches()      # genere tous les matchs
Championnat.play_matches()          # simule le resultat des matchs
Championnat.resultat()              # crée le classement des équipes

# Exemples d'utilisation des méthodes pour obtenir des statistiques
buts_marques = championnat.buts_marque()
buts_encaisses = championnat.buts_encaisse()
VICTOIRENULDEFAITE = championnat.vic_nul_defaite()                      # retourne une liste de listes avec les victoires, nuls et défaites associés au club lors de la fin du championnat
classement_jour = ClassChamp.Calendrier.classement_journee(journee)     # retourne le classement au bout de journee jours. Journee est un entier commencant à 1
Championnat.graphique_buts('Paris Saint Germain')                       # affiche la répartition des buts pour un club, club à rentrer en chaine de caractère correspondant à son nom
Championnat.meilleurs_buteurs()                                         # affiche le graphique des 10 meilleurs buteurs du championnat
