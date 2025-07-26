import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFrame

class InstagramClone(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Instagram UI Clone")
        self.setGeometry(100, 100, 400, 600)
        self.setStyleSheet("background-color: white;")

        # Main Layout
        layout = QVBoxLayout()

        # Header
        header = QFrame(self)
        header.setStyleSheet("background-color: #f8f8f8;")
        header.setFixedHeight(50)
        header_label = QLabel("📷 Insta Clone", self)
        header_label.setAlignment(Qt.AlignCenter)
        header_label.setStyleSheet("font: bold 16px Arial;")
        header_layout = QVBoxLayout()
        header_layout.addWidget(header_label)
        header.setLayout(header_layout)
        layout.addWidget(header)

        # Profile Picture (Placeholder)
        profile_label = QLabel(self)
        pixmap = QPixmap(70, 70)
        pixmap.fill(Qt.lightGray)  # Placeholder gray image
        profile_label.setPixmap(pixmap)
        profile_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(profile_label)

        # Post Area
        post_label = QLabel("✨ Welcome to your Instagram-like UI ✨", self)
        post_label.setAlignment(Qt.AlignCenter)
        post_label.setStyleSheet("font: 12px Arial;")
        layout.addWidget(post_label)

        # Button
        post_button = QPushButton("📩 See Post", self)
        post_button.setStyleSheet("background-color: #0078d4; color: white; font-size: 14px; padding: 10px; border-radius: 5px;")
        post_button.clicked.connect(lambda: post_label.setText("✨ This is a post! ✨"))
        layout.addWidget(post_button)

        # Set Layout
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InstagramClone()
    window.show()
    sys.exit(app.exec_())
