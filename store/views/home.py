from flask import render_template, current_app as app


@app.route('/home', methods=['get', 'post'])
def home():
    return render_template("login.html", title="Login")


@app.route('/register', methods=['get', 'post'])
def rtregister():
    return render_template('register.html', title="Register")


@app.route('/forget', methods=['get', 'post'])
def rtfpwd():
    return render_template('forgetpwd.html', title="Forget")
