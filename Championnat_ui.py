import sys
from PyQt5.Qt import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import  QApplication,QMainWindow, QTableWidgetItem, QTableWidget
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QPixmap
import os
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
        #self.zones(effectifs)
        self.insererImage(self.clubs(effectifs))

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(20)


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


    def zones(self,effectifs):
        C =self.clubs(effectifs)
        L=[]
        for j in range(len(C)):
            cell = QTableWidgetItem(C[j])
            L.append(cell)

        for k in range(len(C)):
            for i in range(2,8):
                    self.tableWidget.setItem(k,i,QTableWidgetItem("0"))

        for l in range(3):
            for m in range(8):
                QTableWidgetItem("0").setBackground(QColor("Green"))
                L[l].setBackground(QColor("Green"))


        for z in range(17,19):
            L[z].setBackground(QColor("Red"))
            for n in range(0,7):
                QTableWidgetItem("0").setBackground(QColor("Red"))



        cell1 = QTableWidgetItem(self.clubs(effectifs)[0])
        cell2 = QTableWidgetItem(self.clubs(effectifs)[1])
        cell3 = QTableWidgetItem(self.clubs(effectifs)[2])
        cell18 = QTableWidgetItem(self.clubs(effectifs)[17])
        cell19= QTableWidgetItem(self.clubs(effectifs)[18])
        cell20 = QTableWidgetItem(self.clubs(effectifs)[19])


        self.tableWidget.setItem(0, 1, cell1)
        self.tableWidget.setItem(1, 1, cell2)
        self.tableWidget.setItem(2, 1, cell3)

        self.tableWidget.setItem(17, 1, cell18)
        self.tableWidget.setItem(18, 1, cell19)
        self.tableWidget.setItem(19, 1, cell20)

        cell1.setBackground(QColor("green"))
        cell2.setBackground(QColor("green"))
        cell3.setBackground(QColor("green"))

        cell18.setBackground(QColor("red"))                 #permet de colorier en vert, le podium, ainsi qu'en rouge, les 3 derniers
        cell19.setBackground(QColor("red"))                 #du classement
        cell20.setBackground(QColor("red"))




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
            self.tableWidget.setItem(row,1,QTableWidgetItem(club))      # on parcours chaque ligne de la table en en sautant une
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


