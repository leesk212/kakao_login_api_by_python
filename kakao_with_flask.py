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
       <img src='/kakao.png'>
    </a>
</body>
</html>'''

@app.route('/oauth')
def oauth():
    code = str(request.args.get('code'))
    print(code)
    return str(code)

if __name__ == '__main__':
    app.run(debug=True)