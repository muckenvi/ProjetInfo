import numpy
import random
import unittest
from typing import List
from datetime import datetime, timedelta

class Club:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def __str__(self):
        return f"{self.name} ({self.city})"

    def effectif(self):
        """
        permet, grace a la lecture d'un fichier texte, d'affecter a chaque equipe l'ensemble de ses joueurs avec
        leurs caracteristiques en faisant appel a la sous classe Joueur
        le fichier texte etant de la forme Joueur, Poste
        """
        effectifs = open('Joueurs championnat.txt')
        a = 0
        for equipes in effectifs:
            effectif = equipes.strip().split(', ')
            if a == 1:
                for i in range(11):
                    self.joueurs.append(Equipe.Joueur(effectif[2 * i], effectif[2 * i + 1], self.nom))
                break
            if effectif[0] == self.nom:
                a = 1
        effectifs.close()


class Joueur:
    def __init__(self, name, number):           # On définit les variables d'instances telles que le nom du joueur
        self.name = name                        # son numéro au club, ainsi que ses stats qui regroupent les buts marqués
        self.name = name                        # et la note attribuée par les journalistes sur ses performances
        self.number = number
        self.stats = {'but': 0, 'note': 0}

    def add_goal(self):                     # Fonction qui améliore le compteur de but du joeur
        self.stats['but'] += 1                      # lorsque ce dernier marque

    def add_note(self, note):               # Même chose pour la note attirbuée
        self.stats['note'] = note

    def __str__(self):                              # Représentation du joueur sous forme de caractère (Nom + numéro)
        return f"{self.name} ({self.number})"




class Match:
    def __init__(self, home, away, home_goals=0, away_goals=0):
        self.home = home
        self.away = away
        self.home_goals = home_goals
        self.away_goals = away_goals

    def play_match(self,championnat):
        home_score = random.randint(0, 5)       # Nombre de buts marqués par l'équipe qui joue à domicile (compris entre 0 et 5)
        away_score = random.randint(0, 5)       # Nombre de buts marqués par l'équipe qui joue à l'extérieur
        self.home_goals = home_score
        self.away_goals = away_score

        if home_score > away_score:                 # Attribution des points en cas de victoire de l'équipe extérieur ou à domicile
            championnat.clubs[self.home] += 3       # ou en cas de match nul
        elif home_score < away_score:
            championnat.clubs[self.away] += 3
        else:
            championnat.clubs[self.away] += 1
            championnat.clubs[self.away] += 1


    def __str__(self):
        return f"{self.home} {self.home_goals} - {self.away_goals} {self.away}"


class Championnat:
    def __init__(self):
        self.clubs = {}
        self.matches = []

    def add_club(self, club):
        self.clubs.update({club : 0})

    def generate_matches(self):         # On génère les matchs pour faire en sorte que chaque équipe rencontre deux fois
        c = list(self.clubs)            # exactement les autres équipes du championnat (ext + domi)
        for i in range(len(c)):         # On réalise donc une double boucle for pour faire cela en tenant compte des indices
            for j in range(i+1, len(c)):    # Pour éviter d'avoir des doublons
                match = Match(c[i], c[j])
                self.matches.append(match)      # On ajoute les différents matchs dans la liste définie dans le constructeur

    def play_matches(self):
        for match in self.matches:
            match.play_match(self)

    def __str__(self):
        classement = []
        for cle, val in self.clubs.items():
            classement.append((cle, val))
        classement = sorted(classement, key=lambda x: x[1], reverse=True)
        classement_str = ""
        rang = 1
        for club, points in classement:
            classement_str += f"{rang}. {club} - {points} points\n"
            rang += 1
        return classement_str




class TestChampionnat(unittest.TestCase):
    def setUp(self):
        self.championnat = Championnat()
        self.club




class Calendrier:
    def __init__(self, debut: datetime, nb_journees: int, journees_par_semaine: int, clubs: List[str]):
        self.debut = debut
        self.nb_journees = nb_journees
        self.journees_par_semaine = journees_par_semaine
        self.clubs = clubs
        self.matchs = {}
        self.calculer_calendrier()

    def calculer_calendrier(self):
        for journee in range(1, self.nb_journees+1):        # On détermine tous les matchs pour chacunes des journées
            journee_matchs = []
            for i, club1 in enumerate(self.clubs):
                for j, club2 in enumerate(self.clubs):
                    if i < j:
                        journee_matchs.append((club1, club2))
            self.matchs[journee] = journee_matchs
    #       matchs est une liste comprenant des listes de tous les matchs des jours

    def get_matchs_journee(self, journee: int) -> List[str]:
        matchs = self.matchs.get(journee, [])
        return ["{} - {}".format(c1, c2) for c1, c2 in matchs]

    def get_date_journee(self, journee: int) -> str:
        journee_date = self.debut + timedelta(days=(journee-1)*7/self.journees_par_semaine)
        return journee_date.strftime("%Y-%m-%d")



