from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import requests
import json


CLIENT_ID = '8d323fc0c13720cda59983912f875316'
REDIRECT_URL = 'https://163.152.126.126:3000/kakao_oauth'
GET_KAKAO_AUTHENTICATION_CODE = 'https://kauth.kakao.com/oauth/authorize?client_id=' + CLIENT_ID + \
                                '&redirect_uri=' + REDIRECT_URL + '&response_type=code'
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
        self.browser.setUrl(QUrl(GET_KAKAO_AUTHENTICATION_CODE))
        self.browser.loadFinished.connect(self.load_finished)
        self.layout.addWidget(self.browser)
        self.setLayout(self.layout)
    def get_response(self, text):
        print(text)
    def load_finished(self):
        print("load_finished")
        page = self.browser.page()
        page.toPlainText(lambda code: get_access_token(code))

def get_access_token(code):
    try:
        print("kakao code: " + code)
        url = "https://kauth.kakao.com/oauth/token"
        payload ={"grant_type": "authorization_code", "client_id": CLIENT_ID, "redirect_uri": REDIRECT_URL, "code": code}
        print(payload)
        headers = {
            'Content-Type': "application/x-www-form-urlencoded",
            'Cache-Control': "no-cache",
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        access_token = json.loads(((response.text).encode('utf-8')))['access_token']
        print("access token: " + access_token)
        url = "https://kapi.kakao.com/v1/user/signup"
        headers.update({'Authorization':"Bearer " + access_token})
        response = requests.request("POST", url, headers=headers)
        print("signup response: " + response.text)
        url = "https://kapi.kakao.com/v1/user/me"
        response = requests.request("POST", url, headers=headers)
        print("me response: " + response.text)

    except Exception as ex:
        print(ex)
class Manager:
    def __init__(self):
        self.window = BrowserWindow()
        self.window.show()
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    manager = Manager()
    sys.exit(app.exec_())