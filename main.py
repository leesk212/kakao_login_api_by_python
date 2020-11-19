from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import requests
import webbrowser
import json


CLIENT_ID = '8d323fc0c13720cda59983912f875316'
REDIRECT_URL = 'http://localhost:5000/oauth'
GET_KAKAO_AUTHENTICATION_CODE = 'https://kauth.kakao.com/oauth/authorize?client_id=' + CLIENT_ID + \
                                '&redirect_uri=' + REDIRECT_URL + '&response_type=code'

print(GET_KAKAO_AUTHENTICATION_CODE)
#a = webbrowser.open(GET_KAKAO_AUTHENTICATION_CODE)
response = requests.get(GET_KAKAO_AUTHENTICATION_CODE)
print(response.url)


#https://163.152.126.126:3000/kakao_oauth?code=atFG_B7bYE524SMaFXdyZ5UbabelJbOwzRGrTAup1FXvMy8S6wXFWQ50uRV4b0OcgBcMMwopcBMAAAF137Y76Q