from PySide6 import QtCore, QtWidgets, QtGui
import main

class MenuWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize window title
        self.setWindowTitle("Coin Chase")
        self.setFixedSize(400, 140)

        # Setup layout
        main_layout = QtWidgets.QVBoxLayout()
        first_layout = QtWidgets.QHBoxLayout()
        second_layout = QtWidgets.QHBoxLayout()
        third_layout = QtWidgets.QHBoxLayout()
        main_layout.addLayout(first_layout)
        main_layout.addLayout(second_layout)
        main_layout.addLayout(third_layout)

        # Add title to window=
        title = QtWidgets.QLabel("Coin Chase")
        title.setFont(QtGui.QFont("Arial", 25))
        title.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        first_layout.addWidget(title)

        # Add label for setting
        map_size = QtWidgets.QLabel("Map Size: ")
        map_size.setFont(QtGui.QFont("Arial", 15))
        map_size.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        second_layout.addWidget(map_size)

        # Dropdown for map sizes
        map_sizes = QtWidgets.QComboBox()
        map_sizes.addItems(["", "32x32", "64x64"])
        third_layout.addWidget(map_sizes)
        map_sizes.activated.connect(self.map_selection)

        # Main widget to display all widgets
        main_widget = QtWidgets.QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def map_selection(self, index):
        with open("test.txt", "w") as f:
            f.write(str(index))

        main_game = main.Main()
        main_game.close_window()
        self.close()

app = QtWidgets.QApplication([])
window = MenuWindow()
window.show()
app.exec()