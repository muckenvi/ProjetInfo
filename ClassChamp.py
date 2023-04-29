import numpy as np
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


class Joueur:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.stats = {'but': 0, 'note': 0}

    def add_goal(self):
        self.stats['but'] += 1

    def add_note(self, note):
        self.stats['note'] = note

    def __str__(self):
        return f"{self.name} ({self.number})"


class Match:
    def __init__(self, home, away, home_goals=0, away_goals=0):
        self.home = home
        self.away = away
        self.home_goals = home_goals
        self.away_goals = away_goals

    def play_match(self,championnat):
        home_score = random.randint(0, 5)
        away_score = random.randint(0, 5)
        self.home_goals = home_score
        self.away_goals = away_score

        if home_score > away_score:
            championnat.clubs[self.home] += 3
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

    def generate_matches(self):
        c = list(self.clubs)
        for i in range(len(c)):
            for j in range(i+1, len(c)):
                match = Match(c[i], c[j])
                self.matches.append(match)

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
        for journee in range(1, self.nb_journees+1):
            journee_date = self.debut + timedelta(days=(journee-1)*7/self.journees_par_semaine)
            journee_matchs = []
            for i, club1 in enumerate(self.clubs):
                for j, club2 in enumerate(self.clubs):
                    if i < j:
                        journee_matchs.append((club1, club2))
            self.matchs[journee] = journee_matchs

    def get_matchs_journee(self, journee: int) -> List[str]:
        matchs = self.matchs.get(journee, [])
        return ["{} - {}".format(c1, c2) for c1, c2 in matchs]

    def get_date_journee(self, journee: int) -> str:
        journee_date = self.debut + timedelta(days=(journee-1)*7/self.journees_par_semaine)
        return journee_date.strftime("%Y-%m-%d")



