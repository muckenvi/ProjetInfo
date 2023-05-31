import unittest
from math import factorial, exp
import random
from itertools import combinations
import Club, Joueur, Match, Championnat

class TestChampionnat(unittest.TestCase):
    def setUp(self):
        """exécutée avant chaque test et permet de préparer les données nécessaires pour les tests.
    Elle crée une instance du championnat, génère les matchs, simule les matchs et calcule le classement."""
        self.championnat = Championnat(Club)
        self.championnat.effectif()
        self.championnat.generate_matches()
        self.championnat.play_matches()
        self.championnat.resultat()

    def test_nombre_matchs(self):
        """ vérifie que le nombre de journées de championnat est égal au nombre de clubs moins un."""
        nb_clubs = len(self.championnat.clubs)
        nb_journees = len(self.championnat.matches) / (nb_clubs / 2)
        self.assertEqual(nb_journees, nb_clubs - 1)

    def test_nombre_points(self):
        """vérifie que le nombre de points distribués lors d'un match est compris entre 2 et
         4 (2 pour un match nul, 3 ou 4 pour une victoire)."""
        for match in self.championnat.matches:
            self.assertIn(match.home_goals + match.away_goals, [2, 3, 4])

    def test_matchs_equipes(self):
        """ vérifie que chaque club a joué exactement deux fois contre chacun des autres clubs."""
        clubs = list(self.championnat.clubs.values())
        for club1, club2 in combinations(clubs, 2):
            nb_matchs = 0
            for match in self.championnat.matches:
                if (match.home == club1 and match.away == club2) or (match.home == club2 and match.away == club1):
                    nb_matchs += 1
            self.assertEqual(nb_matchs, 2)

    def test_classement(self):
        """vérifie que le classement est correctement établi, c'est-à-dire que les équipes
        sont classées par ordre décroissant de points."""
        classement = self.championnat.classement
        prev_note = float('inf')
        for _, note in classement:
            self.assertLessEqual(note, prev_note)
            prev_note = note


if __name__ == '__main__':
    unittest.main()
