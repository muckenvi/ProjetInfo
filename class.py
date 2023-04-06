import numpy as np
import random
import unittest


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

    def play_match(self):
        home_score = random.randint(0, 5)
        away_score = random.randint(0, 5)
        self.home_goals = home_score
        self.away_goals = away_score

        if home_score > away_score:
            self.home.add_points(3)
        elif home_score < away_score:
            self.away.add_points(3)
        else:
            self.home.add_points(1)
            self.away.add_points(1)

    def __str__(self):
        return f"{self.home} {self.home_goals} - {self.away_goals} {self.away}"


class Championnat:
    def __init__(self):
        self.clubs = []
        self.matches = []

    def add_club(self, club):
        self.clubs.append(club)

    def generate_matches(self):
        for i in range(len(self.clubs)):
            for j in range(i + 1, len(self.clubs)):
                match = Match(self.clubs[i], self.clubs[j])
                self.matches.append(match)

    def play_matches(self):
        for match in self.matches:
            match.play_match()

    def get_classement(self):
        return sorted(self.clubs, key=lambda club: (club.points, club.goals_for - club.goals_against), reverse=True)

    def __str__(self):
        classement = self.get_classement()
        classement_str = ""
        for i, club in enumerate(classement):
            classement_str += f"{i + 1}. {club} - {club.points} points\n"
        return classement_str




class TestChampionnat(unittest.TestCase):
    def setUp(self):
        self.championnat = Championnat()
        self.club