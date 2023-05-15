import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.uic import loadUi


class Ligue1App(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Joueurs championnat.txt", self)  # Chargement de l'interface utilisateur

        # Exemple de données pour remplir la table
        data = [
            ("Paris Saint-Germain", "PSG", "1"),
            ("Olympique de Marseille", "OM", "2"),
            ("Olympique Lyonnais", "OL", "3"),
            ("AS Monaco", "MON", "4"),
            ("Lille OSC", "LOSC", "5")
        ]

        # Remplir la table avec les données
        self.fill_table(data)

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ligue1App()
    window.show()
    sys.exit(app.exec_())