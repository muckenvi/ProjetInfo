import sys
from PyQt5.Qt import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import  QApplication,QMainWindow, QTableWidgetItem, QTableWidget
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QPixmap
import os

from PyQt5.QtCore import Qt
import ClassChamp,projet


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
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(20)
        self.rename_column(3,"Nuls")
        self.rename_column(4, "Defaites")
        self.rename_column(5, "Buts marqués")
        self.rename_column(6, "Buts encaissés")
        self.rename_column(7, "Différence de buts")

        self.init_table_with_zeros()
        self.zonesEUROPE()
        self.zonesDESCENTE()

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
        fichier.close()

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










    '''
    def fill_table(self, data):
        # Récupérer le nombre de lignes et de colonnes de la table
        num_rows = len(data)
        num_cols = len(data[0])

        # Définir le nombre de lignes et de colonnes de la table
        self.tableWidget.setRowCount(num_rows)
        self.tableWidget.setColumnCount(num_cols)

        # Parcourir les données et les insérer dans la table
        for row, row_data in enumerate(data):
            for col, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.tableWidget.setItem(row, col, item)

        # Redimensionner automatiquement les colonnes pour ajuster leur contenu
        self.tableWidget.resizeColumnsToContents()
    '''

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





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ligue1()
    window.show()
    sys.exit(app.exec_())


