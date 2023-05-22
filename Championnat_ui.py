import sys
from PyQt5 import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.uic import loadUi


class Ligue1Tableau(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Joueurs championnat.txt", self)  # Chargement de l'interface utilisateur
        set.tableWidget.setColumnWidth(0,100) # Initialisation
        set.tableWidget.setColumnWidth(1, 200)
        set.tableWidget.setColumnWidth(2, 200)

        effectifs= open('Joueurs championnat.txt')
        for equipes in effectifs:
            effectif = equipes.strip().split(', ')

        # Remplir la table avec les données
        self.remplir_table(effectif)

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ligue1Tableau()
    window.show()
    sys.exit(app.exec_())


