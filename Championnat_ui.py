import sys
from PyQt5.Qt import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication

class Ligue1Tableau(QDialog):
    def __init__(self):
        super(Ligue1Tableau,self).__init__()
        loadUi("ChampionnatLigue1.ui", self)  # Chargement de l'interface utilisateur

        self.tableWidget.setColumnWidth(0, 200) # Initialisation
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 200)

        effectifs= open('Joueurs championnat.txt')
        for equipes in effectifs:
            effectifs = equipes.strip().split(', ')

        # Remplir la table avec les données
        self.remplir_table(effectifs)

    def remplir_table(self, fichier):
        # Récupérer le nombre de lignes et de colonnes de la table
        num_lignes = len(fichier)
        num_cols = len(fichier[0])

        # Définir le nombre de lignes et de colonnes de la table
        self.tableWidget.setRowCount(num_lignes)
        self.tableWidget.setColumnCount(num_cols)

        # Parcourir les données et les insérer dans la table
        for ligne, ligne_fichier in enumerate(fichier):
            for col, col_fichier in enumerate(ligne_fichier):
                item = QTableWidgetItem(str(col_fichier))
                self.tableWidget.setItem(ligne, col, item)

        # Redimensionner automatiquement les colonnes pour ajuster leur contenu
        self.tableWidget.resizeColumnsToContents()

app = QApplication(sys.argv)
Ligue1= Ligue1Tableau()
widget = QtWidgets.QStackedWidget()
widget.addWidget(Ligue1)
widget.setFixedHeight(850)
widget.setFixedWidth(1120)

widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exciting")


