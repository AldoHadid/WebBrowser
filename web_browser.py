import os
import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # SET WINDOW TITTLE AND ICON
        self.setWindowTitle("Wacky Wohoo Pizza man")
        self.setWindowIcon(QIcon(os.path.join('icons', 'Nero_DMC5.png')))

        # Navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        # Tombol Back
        back_btn = QAction(QIcon(os.path.join('icons', 'previous_btn.jpg')), "Back", self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        # Tombol Forward
        forward_btn = QAction(QIcon(os.path.join('icons', 'next_btn.jpg')), 'Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        # Tombol Reload
        reload_btn = QAction(QIcon(os.path.join('icons', 'reload_btn.jpg')),'Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        # Tombol Home
        home_btn = QAction(QIcon(os.path.join('icons', 'home_btn.jpg')),'Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        # Tombol Stop
        stop_btn = QAction(QIcon(os.path.join('icons', 'stop_btn.jpg')),'Stop', self)
        stop_btn.triggered.connect(self.browser.stop)
        navbar.addAction(stop_btn)

        # Garis tombol url
        navbar.addSeparator()

        # Mengisi Url
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

        # Help menu
        help_menu = self.menuBar().addMenu("&Help")

        # ADD HELP MENU ACTIONS
        navigate_rickroll_action = QAction('How to...', self)
        help_menu.addAction(navigate_rickroll_action)

        # Never Gonna Give You Up
        navigate_rickroll_action.triggered.connect(self.navigate_rickroll)

        # Menambah StyleSheet
        self.setStyleSheet("""QWidget{
           background-color: rgb(48, 48, 48);
           color: rgb(255, 255, 255);
        }
        QTabWidget::pane { /* The tab widget frame */
            border-top: 2px solid rgb(90, 90, 90);
            position: absolute;
            top: -0.5em;
            color: rgb(1000, 1000, 1000);
            padding: 5px;
        }

        QTabWidget::tab-bar {
            alignment: left;
        }

        /* Style the tab using the tab sub-control. Note that
            it reads QTabBar _not_ QTabWidget */
        QLabel, QToolButton, QTabBar::tab {
            background: rgb(1000, 1000, 1000);
            border: 2px solid rgb(90, 90, 90);
            /*border-bottom-color: #C2C7CB; /* same as the pane color */
            border-radius: 10px;
            min-width: 8ex;
            padding: 5px;
            margin-right: 2px;
            color: rgb(255, 255, 255);
        }

        QLabel:hover, QToolButton::hover, QTabBar::tab:selected, QTabBar::tab:hover {
            background: rgb(49, 49, 49);
            border: 2px solid rgb(0, 66, 124);
            background-color: rgb(0, 36, 36);
        }

        QLineEdit {
            border: 2px solid rgb(0, 36, 36);
            border-radius: 10px;
            padding: 5px;
            background-color: rgb(1000, 1000, 1000);
            color: rgb(255, 255, 255);
        }
        QLineEdit:hover {
            border: 2px solid rgb(0, 100, 0);
        }
        QLineEdit:focus{
            border: 2px solid rgb(0, 136, 255);
            color: rgb(200, 200, 200);
        }
        QPushButton{
            background: rgb(49, 49, 49);
            border: 2px solid rgb(0, 36, 36);
            background-color: rgb(0, 36, 36);
            padding: 5px;
            border-radius: 10px;
        }""")

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def navigate_rickroll(self):
        self.browser.setUrl(QUrl('https://www.youtube.com/watch?v=QDia3e12czc'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName('Browser Progjar')
window = MainWindow()
app.exec_()
