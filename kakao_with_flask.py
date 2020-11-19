from flask import Flask, render_template, redirect, url_for, request, make_response
import requests
import json

CLIENT_ID = '8d323fc0c13720cda59983912f875316'
REDIRECT_URL = 'http://localhost:5000/oauth'
GET_KAKAO_AUTHENTICATION_CODE = 'https://kauth.kakao.com/oauth/authorize?client_id=' + CLIENT_ID + \
                                '&redirect_uri=' + REDIRECT_URL + '&response_type=code'

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
    <a href=" ''' + GET_KAKAO_AUTHENTICATION_CODE + ''' ">
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
    resp = json.loads(json.dumps(response.text, ensure_ascii=False))
    resp_list = list(map(str, resp.split('"')))

    resp_list_p = list()
    for i in range(len(resp_list)):
        if len(resp_list[i]) > 2:
            resp_list_p.append(resp_list[i])
    resp_list = resp_list_p

    nickname = resp_list[resp_list.index('nickname') + 1].replace(" ' ", "")
    email = resp_list[resp_list.index('email') + 1].replace(" ' ", "")
    gender = resp_list[resp_list.index('gender') + 1].replace(" ' ", "")
    birthday = resp_list[resp_list.index('birthday') + 1].replace(" ' ", "")
    profile_image = resp_list[resp_list.index('profile_image') + 1].replace(" ' ", "")

    return '''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>index</title>
    </head>
    <body>
        <img src=' ''' + profile_image + ''' '>
        <p>My Name is ''' + nickname + ''' </p>
        <p>My email is ''' + email + ''' </p>
        <p>My gender is ''' + gender + ''' </p>
        <p>My birthday is ''' + birthday + ''' </p>
    </body>
    </html>'''

if __name__ == '__main__':
    app.run(debug=True)

# https://dydrlaks.medium.com/flask-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EC%82%AC%EC%9A%A9%EC%9E%90%EA%B4%80%EB%A6%AC-rest-api-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0-e07ff5aff018
