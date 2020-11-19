from flask import Flask, render_template, redirect, url_for,request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>index</title>
</head>
<body>
    <a href="https://kauth.kakao.com/oauth/authorize?client_id=8d323fc0c13720cda59983912f875316&redirect_uri=http://localhost:5000/oauth&response_type=code">    
       <img src='https://github.com/leesk212/kakao_login_api_by_python/blob/main/kakao.png?raw=true'>
    </a>
</body>
</html>'''

@app.route('/oauth')
def oauth():
    code = str(request.args.get('code'))
    CLIENT_ID = '8d323fc0c13720cda59983912f875316'
    REDIRECT_URL = 'http://localhost:5000/oauth'
    print('user_code: ' + code)
    url = "https://kauth.kakao.com/oauth/token"
    payload = {"grant_type": "authorization_code", "client_id": CLIENT_ID, "redirect_uri": REDIRECT_URL, "code": code}
    print(payload)
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }
    response = requests.request("POST", url, data=payload)
    access_token = json.loads(((response.text).encode('utf-8')))['access_token']
    print("access token: " + access_token)
    url = "https://kapi.kakao.com/v1/user/signup"
    headers.update({'Authorization': "Bearer " + access_token})
    response = requests.request("POST", url, headers=headers)
    print("signup response: " + response.text)
    url = "https://kapi.kakao.com/v2/user/me"
    response = requests.request("POST", url, headers=headers)
    print("me response: " + response.text)

    return response.text

if __name__ == '__main__':
    app.run(debug=True)