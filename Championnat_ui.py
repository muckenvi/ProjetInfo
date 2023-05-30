import sys

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import  QApplication,QMainWindow, QTableWidgetItem, QTableWidget
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QPixmap
import os

from PyQt5.QtCore import Qt

import ClassChamp
from PyQt5 import QtGui

import projet
from projet import Championnat

class Ligue1(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("ChampionnatLigue.ui", self)  # Chargement de l'interface utilisateur

        column_count = self.tableWidget.columnCount()
        row_count = self.tableWidget.rowCount()

        for i in range(row_count):
            self.tableWidget.setRowHeight(i,150)

        for j in range(column_count):
            self.tableWidget.setColumnWidth(j,150)


        # Exemple de données pour remplir la table

        effectifs = open('Joueurs championnat.txt')
        self.remplir_table(self.clubs(effectifs))

        self.insererImage(self.clubs(effectifs))


        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setRowCount(20)
        self.rename_column(3,"Journée")
        self.rename_column(4, "Victoires")
        self.rename_column(5, "Nuls")
        self.rename_column(6, "Défaites")
        self.rename_column(7, "Buts marqués")
        self.rename_column(8, "Buts encaissés")
        self.rename_column(9, "Différence de buts")

        self.init_table_with_zeros()
        self.zonesEUROPE()
        self.zonesDESCENTE()
        self.pushButton.clicked.connect(self.commande)



        palette = QtGui.QPalette()
        pixmap = QtGui.QPixmap("stade-de-france.jpg.avif")
        caled_pixmap = pixmap.scaled(self.size(), QtCore.Qt.IgnoreAspectRatio)

        palette.setBrush(QtGui.QPalette.Background,QtGui.QBrush(caled_pixmap))
        self.setPalette(palette)



        self.tableWidget.move((self.size().width()- self.tableWidget.width())/2 , (self.size().height() - self.tableWidget.height())/2 )



        self.image_label = QtWidgets.QLabel(self)
        self.image2_label = QtWidgets.QLabel(self)
        pixmap2 = QPixmap("logo.png")
        pixmap2bis = QPixmap("logo.png")
        self.image_label.setPixmap(pixmap2)
        self.image2_label.setPixmap(pixmap2bis)
        self.image_label.setFixedSize(pixmap2.width(), pixmap2.height())
        self.image2_label.setFixedSize(pixmap2bis.width(), pixmap2bis.height())
        self.image_label.move(50, 100)
        self.image2_label.move(1175, 100)


    def commande(self):
        # Code exécuté lorsque le bouton est cliqué
        M=[]
        L= projet.Championnat.resultat()
        for i in range(len(L)):
            M.append(L[i][0])
        self.insererImage2(self.construire_liste_logos(L))
        self.DebutChampionnat(M)
        self.zonesEUROPE()
        self.zonesDESCENTE()
        self.insererImage2(self.construire_liste_logos(L))





    def boutonclique(self):
        self.commande()



    def rename_column(self, column_index, new_name):
        header_item = QTableWidgetItem(new_name)
        self.tableWidget.setHorizontalHeaderItem(column_index, header_item)

    def clubs(self,fichier):
        C=[]
        a = 0
        for equipes in fichier:
            effectif = equipes.strip().split(', ')      #Ontraite le fichier texte pour avoir une liste uniquement avec les
            if a % 3 == 0:                              #clubs
                name = effectif[0]
                C.append(name)
            a += 1
        return C


        # Remplir la table avec les données

                             #on fait appel à notre fonction remplir_table qui permet de rentrer

    def init_table_with_zeros(self):
        rows = self.tableWidget.rowCount()
        cols = self.tableWidget.columnCount()

        for row in range(rows):
            for col in range(cols):
                if col!=0 and col!=1:
                    item = QTableWidgetItem("0")
                    item.setTextAlignment(Qt.AlignCenter)
                    self.tableWidget.setItem(row, col, item)


    def zonesEUROPE(self):
        """ Permet de colorier la zone des clubs qui jouent les places européennes"""
        colonne = int(self.tableWidget.columnCount())
        for col in range(colonne):
            for l in range(3):
                if col !=0:
                    self.tableWidget.item(l,col).setBackground(QColor("Green"))
            for l in range(3,5):
                if col !=0:
                    self.tableWidget.item(l,col).setBackground(QColor("darkGreen"))



    def zonesDESCENTE(self):
        """Permet de colorier la zone des clubs qui jouent le maintien"""

        colonne = int(self.tableWidget.columnCount())
        for ligne in range(17,20):
            for col in range(colonne):
                if col !=0:
                    if ligne ==17 :
                         self.tableWidget.item(ligne,col).setBackground(QColor("darkRed"))
                    else:
                        self.tableWidget.item(ligne,col).setBackground(QColor("Red"))


    def DebutChampionnat(self,M):
        row=0
        # Parcourir les données et les insérer dans la table
        for club in M:
            item=QTableWidgetItem(club)
            self.tableWidget.setItem(row,1,item)
            item.setTextAlignment(Qt.AlignCenter)                       # on parcours chaque ligne de la table en en sautant une
            row+=1








    def remplir_table(self, fichier):
        # Récupérer le nombre de lignes et de colonnes de la table
        num_lignes = len(fichier)
        num_cols = 3

        # Définir le nombre de lignes et de colonnes de la table

        self.tableWidget.setRowCount(num_lignes)
        self.tableWidget.setColumnCount(num_cols)
        row=0
        # Parcourir les données et les insérer dans la table
        for club in fichier:
            item=QTableWidgetItem(club)
            self.tableWidget.setItem(row,1,item)
            item.setTextAlignment(Qt.AlignCenter)                       # on parcours chaque ligne de la table en en sautant une
            row+=1                                                         #à chaque fois qu'on rentre un club dans le tableau

    def Def_image(self, image_path):
        '''
        Charger une image avec QPixmap
        :param image_path: chemin d'accès à l'image
        :return: un QtWidget chargé avec une image
        '''
        image = QtWidgets.QLabel(self.centralWidget())
        pixmap = QPixmap(image_path)
        image.setPixmap(pixmap)
        return image

    def construire_liste_logos(self,effectif):
        base_url = "./Club."

        liste_logos = []

        for club in effectif:
            logo_url = base_url + str(club) + ".png"
            liste_logos.append(logo_url)

        return liste_logos

    def insererImage(self,fichier):
        dossier = "./Clubs"
        L=[]
        for fichier in os.listdir(dossier):
            chemin_fichier = os.path.join(dossier, fichier)
            L.append(self.Def_image(chemin_fichier))

        row=0
        for k in range(len(fichier)+2):

            self.tableWidget.setCellWidget(row,0,L[k])
            row+=1

    def insererImage2(self,fichier):
        L=[]
        for k in range(len(fichier)):

            L.append(self.Def_image(fichier[k]))
        print(L)
        row=0
        for k in range(len(fichier)):

            self.tableWidget.setCellWidget(row,0,L[k])
            row+=1




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ligue1()
    window.show()
    sys.exit(app.exec_())


