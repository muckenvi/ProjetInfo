import random
import unittest
import math
from typing import List
from datetime import datetime, timedelta
import pickle
import matplotlib.pyplot as plt
from math import exp, factorial

class Club():
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self,player):
        self.players.append(player)

    def buts_marques(self,championnat):
        """Retourne le nombre de buts marqués par le club au cours du championnat"""
        buts = 0
        for match in championnat.matches:
            if match.home == self:
                buts += match.home_goals
            elif match.away == self:
                buts += match.away_goals
        return buts

    def buts_encaisses(self, championnat):
        """Retourne le nombre de buts encaissés par le club au cours du championnat"""
        buts = 0
        for match in championnat.matches:
            if match.home == self:
                buts += match.away_goals
            elif match.away == self:
                buts += match.home_goals
        return buts

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

    def poisson_prob(self,lmbda, k):
        return (exp(-lmbda) * (lmbda ** k) )/ factorial(k)

    def simuler_buts(self,lmbda):
        goals = 0

        # Simule le nombre de buts en générant des réalisations de la distribution de Poisson
        while True:
            prob = random.randint(0,2)
            goal_prob = self.poisson_prob(lmbda, goals)

            if prob <= goal_prob:
                break
            else:
                goals += 1

        return goals

    def play_match(self,championnat):
        home_score = self.simuler_buts(30)      # Nombre de buts marqués par l'équipe qui joue à domicile (compris entre 0 et 5)
        away_score = self.simuler_buts(1)      # Nombre de buts marqués par l'équipe qui joue à l'extérieur
        self.home_goals = home_score
        self.away_goals = away_score

        if home_score > away_score:                 # Attribution des points en cas de victoire de l'équipe extérieur ou à domicile
            championnat.clubs[self.home] += 3       # ou en cas de match nul
        elif home_score < away_score:
            championnat.clubs[self.away] += 3
        else:
            championnat.clubs[self.home] += 1
            championnat.clubs[self.away] += 1
        self.attributionNote()
        self.attribuer_buteurs()

    def attributionNote(self):
        home_attaquant = [joueur for joueur in self.home.players if joueur.poste == 'Attaquant']
        away_attaquant = [joueur for joueur in self.away.players if joueur.poste == 'Attaquant']
        home_milieu = [joueur for joueur in self.home.players if joueur.poste == 'Milieu']
        away_milieu = [joueur for joueur in self.away.players if joueur.poste == 'Milieu']
        home_defenseur = [joueur for joueur in self.home.players if joueur.poste == 'Defenseur']
        away_defenseur = [joueur for joueur in self.away.players if joueur.poste == 'Defenseur']
        home_gardien = [joueur for joueur in self.home.players if joueur.poste == 'Gardien']
        away_gardien = [joueur for joueur in self.away.players if joueur.poste == 'Gardien']
        note_min = 4
        note_max = 7
        for joueur in home_attaquant:
            if self.home_goals > self.away_goals:
                note_min += 1
                note_max += 1
            elif self.home_goals < self.away_goals:
                note_min -= 1
                note_max -= 1
            if joueur.poste == 'Gardien' or joueur.poste == 'Defenseur':
                if self.away_goals >= 3:
                    note_min -= 1
                    note_max -= 1
                elif self.away_goals <= 1:
                    note_min += 1
                    note_max += 1
            elif joueur.poste == 'Milieu' or joueur.poste == 'Attaquant':
                if self.home_goals >= 3:
                    note_min += 1
                    note_max += 1
                elif self.home_goals <= 1:
                    note_min -= 1
                    note_max -= 1
            for j in self.home.players:
                if j == joueur:
                    j.add_note(random.randint(note_min, note_max))

    def attribuer_buteurs(self):
        """Attribue aléatoirement aux attaquants de chaque club s'ils ont marqué ou non lors de chaque match"""
        home_attaquant = [joueur for joueur in self.home.players if joueur.poste == 'Attaquant']
        away_attaquant = [joueur for joueur in self.away.players if joueur.poste == 'Attaquant']
        home_milieu = [joueur for joueur in self.home.players if joueur.poste == 'Milieu']
        away_milieu = [joueur for joueur in self.away.players if joueur.poste == 'Milieu']
        home_defenseur = [joueur for joueur in self.home.players if joueur.poste == 'Defenseur']
        away_defenseur = [joueur for joueur in self.away.players if joueur.poste == 'Defenseur']
        home_gardien = [joueur for joueur in self.home.players if joueur.poste == 'Gardien']
        away_gardien = [joueur for joueur in self.away.players if joueur.poste == 'Gardien']

        # Proba attaquants
        buts_h = 0
        buts_a = 0

        while buts_h < self.home_goals:
            # Proba Attaquant
            for attaquant in home_attaquant:
                if random.random() < 0.7 and buts_h < self.home_goals:  # Probabilité de marquer un but, ici 0.5 (modifiable selon les besoins)
                    attaquant.add_goal()
                    buts_h += 1
            # Proba Milieu
            for milieu in home_milieu:
                if random.random() < 0.5 and buts_h < self.home_goals:  # Probabilité de marquer un but, ici 0.5 (modifiable selon les besoins)
                    milieu.add_goal()
                    buts_h += 1

            # Proba Defenseur

            for defenseur in home_defenseur:
                if random.random() < 0.3 and buts_h < self.home_goals:  # Probabilité de marquer un but, ici 0.5 (modifiable selon les besoins)
                    defenseur.add_goal()
                    buts_h += 1

            # Proba Gardien
            for gardien in home_gardien:
                if random.random() < 0.05:  # Probabilité de marquer un but, ici 0.5 (modifiable selon les besoins)
                    gardien.add_goal()
                    buts_h += 1

        while buts_a < self.away_goals:

            for attaquant in away_attaquant:
                if random.random() < 0.63:  # Probabilité de marquer un but, ici 0.5 (modifiable selon les besoins)
                    attaquant.add_goal()
                    buts_a += 1

            for milieu in away_milieu:
                if random.random() < 0.4:  # Probabilité de marquer un but, ici 0.5 (modifiable selon les besoins)
                    milieu.add_goal()
                    buts_a += 1

            for defenseur in away_defenseur:
                if random.random() < 0.25:  # Probabilité de marquer un but, ici 0.5 (modifiable selon les besoins)
                    defenseur.add_goal()
                    buts_a += 1

            for gardien in away_gardien:
                if random.random() < 0.025:  # Probabilité de marquer un but, ici 0.5 (modifiable selon les besoins)
                    gardien.add_goal()
                    buts_a += 1



    def __str__(self):
        return f"{self.home} {self.home_goals} - {self.away_goals} {self.away}"


class Championnat():
    def __init__(self, Club):
        self.Club = Club
        self.clubs = {}
        self.matches = []
        self.classement = []

    def generate_matches(self):         # On génère les matchs pour faire en sorte que chaque équipe rencontre deux fois
        c = list(self.clubs)            # exactement les autres équipes du championnat (ext + domi)
        for i in range(len(c)):         # On réalise donc une double boucle for pour faire cela en tenant compte des indices
            for j in range(i+1, len(c)):    # Pour éviter d'avoir des doublons
                match_aller = Match(c[i], c[j])
                self.matches.append(match_aller)      # On ajoute les différents matchs dans la liste définie dans le constructeur
                match_retour = Match(c[j], c[i])
                self.matches.append(match_retour)      # On ajoute les différents matchs dans la liste définie dans le constructeur


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
                    for cle in self.clubs.keys():
                        if cle.name == name:
                            cle.add_player(Joueur(effectif[2 * i], effectif[2 * i + 1]))
            elif a%3==0:
                name=effectif[0][:-1]
                self.clubs.update({self.Club(name) : 0})
            a+=1
        effectifs.close()

    def resultat(self):
        for cle, val in self.clubs.items():
            self.classement.append((cle.name, val))
        self.classement = sorted(self.classement, key=lambda x: x[1], reverse=True)


    def buts_marque(self):
        buts_m = []
        for club, _ in self.classement:
            for c in self.clubs:
                if club == c.name:
                    buts_m.append(c.buts_marques(self))
        return buts_m

    def buts_encaisses(self):
        buts_m = []
        for club, _ in self.classement:
            for c in self.clubs:
                if club == c.name:
                    buts_m.append(c.buts_encaisses(self))
        return buts_m

    def vic_nul_def(self):
        '''Renvoie trois listes, une pour le nombre de victoire, une pour matchs nuls et une pour les défaites. Le tout dans l'ordre du classement'''
        vic = []
        nul = []
        defaite = []
        for club, _ in self.classement:
            v, n, d = 0, 0, 0
            for m in self.matches:
                if str(club) == str(m.home):
                    if m.home_goals > m.away_goals:
                        v += 1
                    elif m.home_goals == m.away_goals:
                        n += 1
                    else:
                        d += 1
                elif str(club) == str(m.away):
                    if m.away_goals > m.home_goals:
                        v += 1
                    elif m.away_goals == m.home_goals:
                        n += 1
                    else:
                        d += 1
            vic.append(v)
            nul.append(n)
            defaite.append(d)
        return vic, nul, defaite

    def __str__(self):
        classement_str = ""
        rang = 1
        for club, points in self.classement:
            classement_str += f"{rang}. {club} - {points} points\n"
            rang += 1
        return classement_str

    def sauvegarder(self, fichier):
        with open(fichier, 'wb') as f:
            pickle.dump(self, f)

    @staticmethod
    def charger(fichier):
        with open(fichier, 'rb') as f:
            return pickle.load(f)

    def graphique_buts(self, club):
        """graphique de la répartition des buts pour un club"""
        for c in self.clubs.keys():
            if c.name == club:
                joueurs = [j.name for j in c.players]
                buts = [j.stats['but'] for j in c.players]
                plt.pie(buts, labels=joueurs, autopct='%1.1f%%')
                plt.title("Répartition des buts de " + c.name)
                plt.show()

    def meilleurs_buteurs(self):
        joueurs = []
        for c in self.clubs.keys():
            joueurs += c.players
        joueurs = sorted(joueurs, key=lambda x: x.stats['but'], reverse=True)
        plt.bar([j.name for j in joueurs[:10]], [j.stats['but'] for j in joueurs[:10]])
        plt.ylabel("Buts")
        plt.xlabel("Joueurs")
        plt.title("Meilleurs buteurs")
        plt.show()

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
        nb_equipes = len(self.championnat.clubs)
        nb_jours = self.nb_journees//2

        ## matchs allers
        equipes_par_jour = [[] for _ in range(nb_jours)]
        matchs = []
        for m in self.championnat.matches[::2]:
            matchs.append((m.home, m.away))

        # Répartition initiale des matchs sur les jours
        for i, match in enumerate(matchs):
            jour = i % nb_jours
            equipes_par_jour[jour].extend(match)
            self.matchs_par_jour[jour] = [tuple(equipes_par_jour[jour][k:k + 2]) for k in range(0, len(equipes_par_jour[jour]), 2)]

        # Répartition équilibrée des matchs pour chaque équipe
        for equipe in range(1, nb_equipes + 1):
            equipes_jouees = [False] * nb_equipes  # Liste pour chaque équipe, indiquant si elle a déjà joué contre une autre équipe
            for jour in range(nb_jours):
                matchs_jour = self.matchs_par_jour[jour]
                for i, match in enumerate(matchs_jour):
                    if equipe in match:
                        equipe_adverse = match[0] if match[1] == equipe else match[1]
                        if equipes_jouees[equipe_adverse - 1]:
                            # Trouver un autre match où l'équipe n'a pas déjà joué contre l'équipe adverse
                            for j in range(i + 1, len(matchs_jour)):
                                if equipe in matchs_jour[j]:
                                    autre_equipe_adverse = matchs_jour[j][0] if matchs_jour[j][1] == equipe else \
                                        matchs_jour[j][1]
                                    if not equipes_jouees[autre_equipe_adverse - 1]:
                                        # Échanger les équipes adverses
                                        matchs_jour[i] = (equipe, autre_equipe_adverse)
                                        matchs_jour[j] = (equipe_adverse, matchs_jour[j][1] if matchs_jour[j][0] == equipe else matchs_jour[j][0])
                                        break
                        equipes_jouees[equipe_adverse - 1] = True
            self.matchs_par_jour[jour] = matchs_jour
            #fkof
        ## matchs retours
        equipes_par_jour = [[] for _ in range(nb_jours)]
        matchs = []
        for m in self.championnat.matches[1::2]:
            matchs.append((m.home, m.away))

        # Répartition initiale des matchs sur les jours
        for i, match in enumerate(matchs):
            jour = i % nb_jours
            equipes_par_jour[jour].extend(match)
            self.matchs_par_jour[jour+nb_jours] = [tuple(equipes_par_jour[jour][k:k + 2]) for k in range(0, len(equipes_par_jour[jour]), 2)]

        # Répartition équilibrée des matchs pour chaque équipe
        for equipe in range(1, nb_equipes + 1):
            equipes_jouees = [False] * nb_equipes  # Liste pour chaque équipe, indiquant si elle a déjà joué contre une autre équipe
            for jour in range(nb_jours):
                matchs_jour = self.matchs_par_jour[jour+nb_jours]
                for i, match in enumerate(matchs_jour):
                    if equipe in match:
                        equipe_adverse = match[0] if match[1] == equipe else match[1]
                        if equipes_jouees[equipe_adverse - 1]:
                            # Trouver un autre match où l'équipe n'a pas déjà joué contre l'équipe adverse
                            for j in range(i + 1, len(matchs_jour)):
                                if equipe in matchs_jour[j]:
                                    autre_equipe_adverse = matchs_jour[j][0] if matchs_jour[j][1] == equipe else \
                                        matchs_jour[j][1]
                                    if not equipes_jouees[autre_equipe_adverse - 1]:
                                        # Échanger les équipes adverses
                                        matchs_jour[i] = (equipe, autre_equipe_adverse)
                                        matchs_jour[j] = (equipe_adverse, matchs_jour[j][1] if matchs_jour[j][0] == equipe else matchs_jour[j][0])
                                        break
                        equipes_jouees[equipe_adverse - 1] = True
            self.matchs_par_jour[jour+nb_jours] = matchs_jour

    def get_matchs_journee(self, journee):
        matchs = self.matchs_par_jour[journee-1]
        for match in matchs:
            for m in self.championnat.matches:
                if m.home == match[0] and m.away == match[1]:
                    print(m)

    def get_date_journee(self, journee: int) -> str:
        journee_date = self.debut + timedelta(days=(journee-1)*7/self.journees_par_semaine)
        return journee_date.strftime("%Y-%m-%d")

    def classement_journee(self, journee):
        classement_j = {}
        class_j = []
        for m in self.matchs_par_jour[journee-1]:       # parcours des matchs du jour
            for match in self.championnat.matches:      # parcours des matchs du championnat
                if match.home == m[0] and match.away == m[1]:
                    if match.home_goals > match.away_goals:                 # Attribution des points en cas de victoire de l'équipe extérieur ou à domicile
                        if match.home.name not in classement_j:
                            classement_j.update({match.home.name : 0})
                        classement_j[match.home.name] += 3       # ou en cas de match nul
                    elif match.home_goals < match.away_goals:
                        if match.away.name not in classement_j:
                            classement_j.update({match.away.name : 0})
                        classement_j[match.away.name] += 3
                    else:
                        if match.home.name not in classement_j:
                            classement_j.update({match.home.name : 0})
                        if match.away.name not in classement_j:
                            classement_j.update({match.away.name : 0})
                        classement_j[match.home.name] += 1
                        classement_j[match.away.name] += 1
        for cle, val in classement_j.items():
            class_j.append((cle, val))
        class_j = sorted(class_j, key=lambda x: x[1], reverse=True)
        return class_j