# The project is a browser called pelican


# PyQt5 is a library that is adding widgets and Gui to python it also has a widget
# called webengine which has useful functions for website creating
# sys is just what we use to run the program
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
import sys


# mainwindows class that acullty makes the window and maximizes it
class MainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.google.com/'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        navbar = QToolBar()
        self.addToolBar(navbar)

        navbar.addSeparator()
        # back button that takes the page backwards into your search history
        back_btn = QAction('←', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)
        # navbar .addseperator just adds a line between the two button
        navbar.addSeparator()
        # foreword button that takes the page forwards into your search history
        frd_btn = QAction('→', self)
        frd_btn.triggered.connect(self.browser.forward)
        navbar.addAction(frd_btn)

        navbar.addSeparator()
        # this is the reload button is reloads the page u are on
        rld_btn = QAction('֎', self)
        rld_btn.triggered.connect(self.browser.reload)
        navbar.addAction(rld_btn)

        navbar.addSeparator()
        # home button which sends you to google.com
        hme_btn = QAction('⌂', self)
        hme_btn.triggered.connect(self.nav_hme)
        navbar.addAction(hme_btn)

        navbar.addSeparator()
        # the url bar is where u type in the url
        # and i added a function that says that if the url changed then it updates to the new url
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.nav_url)
        self.url_bar.setFixedWidth(900)
        navbar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.update_url)

        navbar.addSeparator()

        web_btn = QAction('My Youtube Channel', self)
        web_btn.triggered.connect(self.web_nav)
        navbar.addAction(web_btn)

    def update_url(self, url):
        self.url_bar.setText(url.toString())

    def nav_url(self):
        url = 'https://' + self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def nav_hme(self):
        self.browser.setUrl(QUrl("https://www.google.com"))

    def web_nav(self):
        self.browser.setUrl(QUrl('https://www.youtube.com/channel/UC_ON-2qjme_iIMaBCYg-jfQ/videos'))

    # app line just says that it is an application that requires new windows


app = QApplication(sys.argv)
# this is the place to set the name of the program which i set to pelican
QApplication.setApplicationName('pelican browser')
# this line is an object based of off of the MainWindow class
window = MainWindow()
# this line just runs the app
app.exec_()
