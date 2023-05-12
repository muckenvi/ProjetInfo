import numpy
import random
import unittest
import math
from typing import List
from datetime import datetime, timedelta

class Club():
    def __init__(self, name):
        self.name = name
        self.players = []



    def add_player(self,player):
        self.players.append(player)


    def __str__(self):
        return f"{self.name}"


class Joueur():
    def __init__(self, name,poste):           # On définit les variables d'instances telles que le nom du joueur
        self.name = name
        self.poste = poste                               # son numéro au club, ainsi que ses stats qui regroupent les buts marqués                     # et la note attribuée par les journalistes sur ses performances
        self.stats = {'but': 0, 'note': 0}



    def add_goal(self):                     # Fonction qui améliore le compteur de but du joeur
        self.stats['but'] += 1                      # lorsque ce dernier marque

    def add_note(self, note):               # Même chose pour la note attirbuée
        self.stats['note'] = note

    def __str__(self):                              # Représentation du joueur sous forme de caractère (Nom + numéro)
        return f"{self.name}  poste:{self.poste} stats : {self.stats}"




class Match():
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
            championnat.clubs[self.home] += 1
            championnat.clubs[self.away] += 1


    def __str__(self):
        return f"{self.home} {self.home_goals} - {self.away_goals} {self.away}"


class Championnat():
    def __init__(self):
        self.clubs = {}
        self.matches = []

    def generate_matches(self):         # On génère les matchs pour faire en sorte que chaque équipe rencontre deux fois
        c = list(self.clubs)            # exactement les autres équipes du championnat (ext + domi)
        for i in range(len(c)):         # On réalise donc une double boucle for pour faire cela en tenant compte des indices
            for j in range(i+1, len(c)):    # Pour éviter d'avoir des doublons
                match = Match(c[i], c[j])
                self.matches.append(match)      # On ajoute les différents matchs dans la liste définie dans le constructeur

    def play_matches(self):
        for match in self.matches:
            match.play_match(self)

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
            if a%3==1:
                for i in range(11):
                    Club(name).add_player(Joueur(effectif[2 * i], effectif[2 * i + 1]))
                self.clubs.update({name : 0})
            elif a%3==0:
                name=effectif[0]
                Club(name)
            a+=1
        effectifs.close()

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




class Calendrier():
    def __init__(self, debut: datetime, nb_journees: int, journees_par_semaine: int, clubs: List[str], championnat):
        self.debut = debut
        self.nb_journees = nb_journees
        self.journees_par_semaine = journees_par_semaine
        self.clubs = clubs
        self.matchs_par_jour = {}
        self.championnat = championnat
        self.calculer_calendrier()

    def calculer_calendrier(self):

        """
        Répartit les matchs d'un championnat sur un nombre donné de jours.

        Arguments :
        matchs -- une liste de matchs triée, chaque match étant représenté par un tuple de deux équipes.
        nb_jours -- le nombre de jours sur lesquels répartir les matchs.

        Renvoie :
        Un dictionnaire associant à chaque jour un ensemble de matchs.
        """
        nb_matchs = len(self.championnat.matches)
        nb_matchs_par_jour = math.ceil(nb_matchs / self.nb_journees)
        equipes_jouees = set()
        jour_actuel = 0
        for i, match in enumerate(self.championnat.matches):
            equipe1, equipe2 = match.home, match.away
            if equipe1 in equipes_jouees or equipe2 in equipes_jouees:
                # On essaie de placer le match sur un jour suivant où les deux équipes ne jouent pas
                for j in range(jour_actuel + 1, self.nb_journees + 1):
                    if j not in self.matchs_par_jour:
                        self.matchs_par_jour[j] = set()
                    if len(self.matchs_par_jour[j]) < nb_matchs_par_jour and equipe1 not in equipes_jouees and equipe2 not in equipes_jouees:
                        self.matchs_par_jour[j].add(match)
                        equipes_jouees.add(equipe1)
                        equipes_jouees.add(equipe2)
                        jour_actuel = j
                        break
            else:
                if jour_actuel not in self.matchs_par_jour:
                    self.matchs_par_jour[jour_actuel] = set()
                self.matchs_par_jour[jour_actuel].add(match)
                equipes_jouees.add(equipe1)
                equipes_jouees.add(equipe2)
                if len(self.matchs_par_jour[jour_actuel]) == nb_matchs_par_jour:
                    jour_actuel += 1
                    equipes_jouees.clear()

        # """
        # Répartit les matchs d'un championnat sur un nombre donné de jours.
        #
        # Arguments :
        # matchs -- une liste de matchs, chaque match étant représenté par un tuple de deux équipes.
        # nb_jours -- le nombre de jours sur lesquels répartir les matchs.
        #
        # Renvoie :
        # Un dictionnaire associant à chaque jour un ensemble de matchs.
        # """
        # nb_matchs = len(self.championnat.matches)
        # nb_matchs_par_jour = math.ceil(nb_matchs / self.nb_journees)
        # jour_actuel = 0
        # equipes_jouees = set()
        # for i, match in enumerate(self.championnat.matches):
        #     if i % nb_matchs_par_jour == 0:
        #         jour_actuel += 1
        #         equipes_jouees.clear()
        #     if jour_actuel not in self.matchs_par_jour:
        #         self.matchs_par_jour[jour_actuel] = set()
        #     equipe1, equipe2 = match.home, match.away
        #     if equipe1 not in equipes_jouees and equipe2 not in equipes_jouees:
        #         self.matchs_par_jour[jour_actuel].add(match)
        #         equipes_jouees.add(equipe1)
        #         equipes_jouees.add(equipe2)
        #     else:
        #         # On essaie de placer le match sur un jour suivant où les deux équipes ne jouent pas
        #         for j in range(jour_actuel + 1, self.nb_journees + 1):
        #             if j not in self.matchs_par_jour:
        #                 self.matchs_par_jour[j] = set()
        #                 if equipe1 not in equipes_jouees and equipe2 not in equipes_jouees:
        #                     self.matchs_par_jour[j].add(match)
        #                     equipes_jouees.add(equipe1)
        #                     equipes_jouees.add(equipe2)
        #                     jour_actuel = j
        #                     break
        # # self.matchs_par_jour est une liste des matchs par jour


    def get_matchs_journee(self, journee: int) -> List[str]:
        matchs = self.matchs_par_jour[journee]
        print(self.matchs_par_jour[3])
        for match in matchs:
            print("{} - {}".format(match.home, match.away))

    def get_date_journee(self, journee: int) -> str:
        journee_date = self.debut + timedelta(days=(journee-1)*7/self.journees_par_semaine)
        return journee_date.strftime("%Y-%m-%d")



