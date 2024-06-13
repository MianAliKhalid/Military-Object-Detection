import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, 
    QFileDialog, QHBoxLayout, QSpacerItem, QSizePolicy, QGridLayout
)
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtCore import Qt
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from utils import Get_detected_image

modelpth = 'runs/detect/train/weights/last.pt'

class ImagePlotter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Military Target Detection by Mian Ali Khalid')
        self.setGeometry(100, 100, 400, 400)

        # Main layout
        main_layout = QVBoxLayout()

        # Top layout for logo and close button
        top_layout = QHBoxLayout()

        # Logo label
        logo_label = QLabel(self)
        logo_pixmap = QPixmap('logo.png')  # Update this path to your logo image
        logo_pixmap = logo_pixmap.scaled(300, 300)
        logo_label.setPixmap(logo_pixmap)
        logo_label.setFixedSize(300, 300)  # Adjust size as needed
        top_layout.addWidget(logo_label, alignment=Qt.AlignLeft)

        # Title label
        title_label = QLabel('Military Target Detection By Mian Ali Khalid Chief Scientist at Tech Horizen Pvt Ltd')
        title_label.setFont(QFont('Arial', 20))
        top_layout.addWidget(title_label, alignment=Qt.AlignCenter)

        # Close button
        close_button = QPushButton('Close', self)
        close_button.setFont(QFont('Arial', 12))
        close_button.setStyleSheet("background-color: lightcoral;")
        close_button.clicked.connect(self.close)
        top_layout.addWidget(close_button, alignment=Qt.AlignRight)

        main_layout.addLayout(top_layout)

        # Upload button
        self.btn = QPushButton('Upload Image')
        self.btn.setFont(QFont('Arial', 14))
        self.btn.clicked.connect(self.open_image)
        main_layout.addWidget(self.btn, alignment=Qt.AlignCenter)

        # Image display canvas
        self.canvas = FigureCanvas(plt.Figure())
        self.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        main_layout.addWidget(self.canvas)

        # Status label
        self.label = QLabel('Upload an Image')
        self.label.setFont(QFont('Arial', 14))
        self.label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.label)


        # Set the layout in the main window
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        self.showMaximized()

    def open_image(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", 
                                                  "All Files (*);;Image Files (*.png;*.jpg;*.jpeg;*.bmp)", 
                                                  options=options)
        if fileName:
            self.label.setText(fileName)
            self.display_image(fileName)

    def display_image(self, file_path):
        predicted_image = Get_detected_image(modelpth, file_path)
        img_array = np.array(predicted_image)
        self.canvas.figure.clear()
        ax = self.canvas.figure.add_subplot(111)
        ax.imshow(img_array)
        ax.axis('off')
        self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ImagePlotter()
    sys.exit(app.exec_())
