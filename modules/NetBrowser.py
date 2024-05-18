from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QWidget

class NetBrowserWin():
    def __init__(self):

        self.window = QWidget()
        self.window.setWindowTitle("PyUI_OS Net Browser")
        self.window.resize(800, 600)

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.url_bar = QLineEdit()
        self.url_bar.setMaximumHeight(35)

        self.go_button = QPushButton("Go")
        self.go_button.setMinimumHeight(35)
        self.go_button.setMaximumWidth(75)
        
        self.back_button = QPushButton("<")
        self.back_button.setMinimumHeight(35)
        self.back_button.setMaximumWidth(75)
        
        self.forward_button = QPushButton(">")
        self.forward_button.setMinimumHeight(35)
        self.forward_button.setMaximumWidth(75)

        self.home_button = QPushButton("HOME")
        self.home_button.setMinimumHeight(35)
        self.home_button.setMaximumWidth(75)

        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_button)
        self.horizontal.addWidget(self.back_button)
        self.horizontal.addWidget(self.forward_button)
        self.horizontal.addWidget(self.home_button)

        self.browser = QWebEngineView()

        self.go_button.clicked.connect(lambda: self.navigate(self.url_bar.text()))
        self.url_bar.returnPressed.connect(lambda: self.navigate(self.url_bar.text()))
        self.back_button.clicked.connect(self.browser.back)
        self.forward_button.clicked.connect(self.browser.forward)
        self.home_button.clicked.connect(lambda: self.navigate("http://google.com"))


        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        self.browser.setUrl(QUrl("http://google.com"))

        self.window.setLayout(self.layout)
        self.window.show()

    def navigate(self, url):
        if not url.startswith("http"):
            url = "http://"+url
            self.url_bar.setText(url)

        self.browser.setUrl(QUrl(url))

    def open_browser(self):
        self.window.show()

