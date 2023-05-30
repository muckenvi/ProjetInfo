import random
import unittest
import math
from typing import List
from datetime import datetime, timedelta
import pickle
import matplotlib.pyplot as plt

class Club():
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self,player):
        self.players.append(player)



    def buts_marques(self,championnat, club):
        """Retourne le nombre de buts marqués par le club au cours du championnat"""
        buts = 0
        for match in championnat.matches:
            if match.home == club:
                buts += match.home_goals
            elif match.away == club:
                buts += match.away_goals
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

    def attributionNote(self):
        home_attaquant = [joueur for joueur in self.home.joueur if joueur.poste == 'Attaquant']
        away_attaquant = [joueur for joueur in self.away.joueur if joueur.poste == 'Attaquant']
        home_milieu = [joueur for joueur in self.home.joueur if joueur.poste == 'Milieu']
        away_milieu = [joueur for joueur in self.away.joueur if joueur.poste == 'Milieu']
        home_defenseur = [joueur for joueur in self.home.joueur if joueur.poste == 'Defenseur']
        away_defenseur = [joueur for joueur in self.away.joueur if joueur.poste == 'Defenseur']
        home_gardien = [joueur for joueur in self.home.joueur if joueur.poste == 'Gardien']
        away_gardien = [joueur for joueur in self.away.joueur if joueur.poste == 'Gardien']
        note_min = 4
        note_max = 7
        for match in championnat.matches:
            for joueur in self.home.attaquant:
                if self.home_goals > self.away_goals:
                    note_min += 1
                    note_max += 1
                elif self.home_goals < self.away_goals:
                    note_min -= 1
                    note_max -= 1
                if Joueur.poste == 'Gardien' or Joueur.poste == 'Defenseur':
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
                self.home.players.add_note(random.randint(note_min, note_max))

    def attribuer_buteurs(self, championnat):
        """Attribue aléatoirement aux attaquants de chaque club s'ils ont marqué ou non lors de chaque match"""
        for match in championnat.matches:
            home_attaquant = [joueur for joueur in self.home.joueur if joueur.poste == 'Attaquant']
            away_attaquant = [joueur for joueur in self.away.joueur if joueur.poste == 'Attaquant']
            home_milieu = [joueur for joueur in self.home.joueur if joueur.poste == 'Milieu']
            away_milieu = [joueur for joueur in self.away.joueur if joueur.poste == 'Milieu']
            home_defenseur = [joueur for joueur in self.home.joueur if joueur.poste == 'Defenseur']
            away_defenseur = [joueur for joueur in self.away.joueur if joueur.poste == 'Defenseur']
            home_gardien = [joueur for joueur in self.home.joueur if joueur.poste == 'Gardien']
            away_gardien = [joueur for joueur in self.away.joueur if joueur.poste == 'Gardien']

            # Proba attaquants
            buts_h = 0
            buts_a = 0

            while buts_h < self.home_goals:
                # Proba Attaquant
                for attaquant in home_attaquant:
                    if random.random() < 0.7 and buts < self.home_goals:  # Probabilité de marquer un but, ici 0.5 (modifiable selon les besoins)
                        attaquant.add_goal()
                        buts_h += 1
                # Proba Milieu
                for milieu in home_milieu:
                    if random.random() < 0.5 and buts < self.home_goals:  # Probabilité de marquer un but, ici 0.5 (modifiable selon les besoins)
                        milieu.add_goal()
                        buts_h += 1

                # Proba Defenseur

                for defenseur in home_defenseur:
                    if random.random() < 0.3 and buts < self.home_goals:  # Probabilité de marquer un but, ici 0.5 (modifiable selon les besoins)
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
    def __init__(self):
        self.clubs = {}
        self.matches = []

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
                    Club(name).add_player(Joueur(effectif[2 * i], effectif[2 * i + 1]))
                self.clubs.update({name : 0})
            elif a%3==0:
                name=effectif[0]
                Club(name)
            a+=1
        effectifs.close()

    def resultat(self):
        classement = []
        for cle, val in self.clubs.items():
            classement.append((cle, val))
        classement = sorted(classement, key=lambda x: x[1], reverse=True)
        return classement

    def __str__(self):
        classement_str = ""
        rang = 1
        classement = self.resultat()
        for club, points in classement:
            classement_str += f"{rang}. {club} - {points} points\n"
            rang += 1
        return classement_str



    '''
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
        
    '''

    def sauvegarder(self, fichier):
        with open(fichier, 'wb') as f:
            pickle.dump(self, f)

    @staticmethod
    def charger(fichier):
        with open(fichier, 'rb') as f:
            return pickle.load(f)
    '''
    def graphique_buts(self):
        clubs = [club.name for club in self.clubs]
        buts = [club.buts_marques for club in self.clubs]

        fig, ax = plt.subplots()
        ax.bar(clubs, buts)
        ax.set_xlabel("Club")
        ax.set_ylabel("Buts")
        
    '''





class Calendrier():
    def __init__(self, debut: datetime, nb_journees: int, journees_par_semaine: int, clubs: List[str], championnat):
        self.debut = debut
        self.nb_journees = nb_journees
        self.journees_par_semaine = journees_par_semaine
        self.clubs = clubs
        # self.matchs_par_jour = [[] for _ in range(self.nb_journees)]
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



