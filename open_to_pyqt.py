from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import webbrowser

class BrowserWindow(QMainWindow):
    def __init__(self, parent=None):
        super(BrowserWindow, self).__init__(parent)
        self.setWindowTitle("DB만만 : DB Project")
        self.setGeometry(800, 500, 400, 650)
        self.form_widget = FormWidget(self)
        self.setCentralWidget(self.form_widget)


class FormWidget(QWidget):
    def __init__(self, parent):
        super(FormWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.browser = QWebEngineView(self)
        self.browser.setUrl(QUrl('http://127.0.0.1:5000/'))
        self.browser.loadFinished.connect(self.load_finished)
        self.layout.addWidget(self.browser)
        self.setLayout(self.layout)

    def get_response(self, text):
        print(text)

    def load_finished(self):
        print("load_finished")
        page = self.browser.page()

def open_url():
    try:
        webbrowser.open('https://klas.kw.ac.kr')
    except Exception as ex:
        print(ex)
class Manager:
    def __init__(self):
        self.window = BrowserWindow()
        self.window.show()
        open_url()
        print('a')

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    manager = Manager()
    sys.exit(app.exec_())