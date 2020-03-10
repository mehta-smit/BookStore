import requests
import json

from flask import render_template, current_app as app
from flask import request


from store.engine.utils.call_api import call_api


@app.route('/', methods=['get', 'post'])
@app.route('/home', methods=['get', 'post'])
def home():
    if request.method == "POST":
        login_url = app.config.get("HOST_URL") + "common/login"
        data = request.form

        response = requests.post(login_url, data=json.dumps(data), headers={'content-type': 'application/json'})
        status_code = response.status_code
        text = json.loads(response.text)
        if status_code != 200:
            return dict(status=status_code, message=text.get("message"), error=True)
        return dict(status=status_code, data=text, error=False)
    return render_template("login.html", title="Login")


@app.route('/register', methods=['get', 'post'])
def rtregister():
    if request.method == 'POST':
        signup_url = app.config.get("HOST_URL") + "common/signup"
        response = requests.post(signup_url, data=json.dumps(request.form), headers={'content-type': 'application/json'})
        status_code = response.status_code
        text = json.loads(response.text)
        if status_code != 200:
            return dict(status=status_code, message=text, error=True)
        return dict(status=status_code, data=text, error=False)
    return render_template('register.html', title="Register")


@app.route('/forget', methods=['get', 'post'])
def rtfpwd():
    return render_template('forgetpwd.html', title="Forget")
