import unittest
from ClassChamp import Club, Joueur, Match, Calendrier, Championnat


class TestChampionnat(unittest.TestCase):

    def setUp(self):
        # Création de deux clubs avec des joueurs
        # on prend ici le cas n=4 pour simplifier les tests
        self.club1 = Club("Paris Saint-Germain")
        self.club2 = Club("Olympique de Marseille")
        self.joueur1 = Joueur("Neymar", 10)
        self.joueur2 = Joueur("Kylian Mbappé", 7)
        self.joueur3 = Joueur("Dimitri Payet", 8)
        self.joueur4 = Joueur("Florian Thauvin", 6)
        self.club1.add_player(self.joueur1)
        self.club1.add_player(self.joueur2)
        self.club2.add_player(self.joueur3)
        self.club2.add_player(self.joueur4)

    def test_nombre_de_points(self):
        # Vérification que le nombre de points distribué lors d'une journée
        # est compris entre 2 et 3 fois le nombre de matchs
        calendrier = Calendrier([self.club1, self.club2])
        journee = calendrier.()
        nb_matchs = len(journee)
        nb_points = sum([match.get_points() for match in journee])
        self.assertGreaterEqual(nb_points, 2 * nb_matchs)
        self.assertLessEqual(nb_points, 3 * nb_matchs)

    def test_nombre_de_matchs_par_journee(self):
        # Vérification que le nombre de match par journée ne dépasse pas la moitié du nombre de club
        calendrier = Calendrier([self.club1, self.club2])
        nb_clubs = len(calendrier.clubs)
        journee = calendrier.get_matchs_journee()
        nb_matchs = len(journee)
        self.assertEqual(nb_matchs, nb_clubs // 2)

    def test_resultat_match(self):
        # Vérification qu'un club gagne si le nombre
        # de buts marqués est supérieur à celui de son adversaire
        match = Match(self.club1, self.club2)
        self.joueur1.add_goal(2)
        self.joueur2.add_goal(1)
        self.joueur3.add_goal(1)
        self.assertEqual(match.get_gagnant(), self.club1)


if __name__ == '__main__':
    unittest.main()

