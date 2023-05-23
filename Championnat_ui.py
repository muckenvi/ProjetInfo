import sys
from PyQt5.Qt import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import  QApplication,QMainWindow, QTableWidgetItem, QTableWidget
from PyQt5.QtGui import QColor

'''
class Ligue1Tableau(QDialog):
    def __init__(self):
        super(Ligue1Tableau,self).__init__()
        loadUi("ChampionnatLigue1.ui", self)  # Chargement de l'interface utilisateur

        self.tableWidget.setColumnWidth(0, 200)  # Initialisation
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 200)


        effectifs= open('Joueurs championnat.txt')
        for equipes in effectifs:
            effectifs = equipes.strip().split(', ')

        # Remplir la table avec les données
        self.remplir_table(effectifs)




app = QApplication(sys.argv)
ligue1tableau = Ligue1Tableau()
widget = QtWidgets.QStackedWidget()
widget.addWidget(ligue1tableau)
widget.setFixedHeight(850)
widget.setFixedWidth(1120)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exciting")
'''

class Ligue1(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("ChampionnatLigue1.ui", self)  # Chargement de l'interface utilisateur

        self.tableWidget.setColumnWidth(0, 300)  # Initialisation des colonnes et de leur largeur respective
        self.tableWidget.setColumnWidth(1, 300)
        self.tableWidget.setColumnWidth(2, 300)

        # Exemple de données pour remplir la table

        effectifs = open('Joueurs championnat.txt')

        a = 0
        C=[]
        for equipes in effectifs:
            effectif = equipes.strip().split(', ')      #Ontraite le fichier texte pour avoir une liste uniquement avec les
            if a % 3 == 0:                              #clubs
                name = effectif[0]
                C.append(name)
            a += 1
        print(C)
        effectifs.close()
        # Remplir la table avec les données
        self.remplir_table(C)                               #on fait appel à notre fonction remplir_table qui permet de rentrer
                                                            #chaque nom de club dans le tableau sur qt designer

        cell1 = QTableWidgetItem(C[0])
        cell2 = QTableWidgetItem(C[1])
        cell3 = QTableWidgetItem(C[2])

        cell18 = QTableWidgetItem(C[17])
        cell19 = QTableWidgetItem(C[18])
        cell20 = QTableWidgetItem(C[19])


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





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ligue1()
    window.show()
    sys.exit(app.exec_())

