from flask import Flask, render_template, request, session, escape, redirect, url_for,g
import model
from functools import wraps
from flask_cors import cross_origin

app = Flask(__name__, static_url_path='')
name = "Hello"
# model.createdefaultusers()
app.secret_key = b'(*&%HJVHGFHFCGHHJGHFYHF*&^*%&%&^%*(&*%&5756685756868575234HIUHIHIdfsoijdf'

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' in session:
            uname = escape(session['username'])
            if uname:
                s = model.conn()
                res = s.query(model.User.username).filter_by(username=uname)
                if res[0].username == uname:
                    #return True
                    return f(*args, **kwargs)
                else: 
                    return redirect(url_for('login'))
        else:
            return redirect(url_for('login'))
    return decorated_function

@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html',i=escape(session['username']))
    else:
        return render_template('index.html')

@app.route('/serialization')
@login_required
def serialization():
    return render_template('serialization.html', i=escape(session['username']))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method =='POST':
        if (request.form['repassword'] == request.form['password']):
            s = model.conn()
            user = model.User(username=request.form['username'], password=request.form['password'])
            s.add(user)
            s.commit()
        return render_template('login.html')


@app.route('/secret')
@login_required
def secret():
    return render_template('secret.html', i=escape(session['username']))
    # return "Congrats! You are almost there. Go to the page "

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        s = model.conn()
        res = s.query(model.User.password).filter_by(username=request.form['username'])
        if (res[0].password == request.form['password']) :
            session['username'] = request.form['username']
            # request.cookie.set('username') = request.form['username']
            return render_template('index.html',i = escape(session['username']))
    return render_template('login.html')

@app.route('/cors', methods=['GET', 'POST'])
# @login_required
@cross_origin(origins = '*')
def cors():
    if request.method == 'GET':
        return render_template('cors.html', i=escape(session['username']))
    elif request.method == 'POST':
        if request.form['message']:
            return request.form['message'] + " Get this message cross domain."

@app.route('/4015bc9ee91e437d90df83fb64fbbe312d9c9f05', methods=['GET', 'POST'])
@login_required
def directoryfound1():
    form = [
        { 'posturl': '4015bc9ee91e437d90df83fb64fbbe312d9c9f05', 
        'level': 1, 
        'flag': '987947614649875449846516765449',
        'hint':'R28gdG8gdGhlIHBhZ2UgLzhmMWY3YzliOTRlNTcwYWM4NmZmNzA3ZGUwYTkyOTRmODY4MjU2NjE=' 
        }, 
        { 'posturl': '4015bc9ee91e437d90df83fb64fbbe312d9c9f05', 
        'level': 2, 
        'flag': '987947614649875449846516765449',
        'hint':'R28gdG8gdGhlIHBhZ2UgLzhmMWY3YzliOTRlNTcwYWM4NmZmNzA3ZGUwYTkyOTRmODY4MjU2NjE=' 
        }
    ]
    if request.method == 'GET':
        return render_template('crackcode.html', pin=form[0], i=escape(session['username']))
    else:
        if (request.form['pin']=='9876'):
            return render_template('success.html', pin=form[0], i=escape(session['username']))
        else:
            return render_template('crackcode.html', i=escape(session['username']))


@app.route('/csrf', methods=['GET', 'POST'])
@login_required
def csrf():
    if request.method == 'GET':
        return render_template('csrf.html', i=escape(session['username']))
    elif request.method == 'POST':
        if request.form['password']:
           s = model.conn()
           res = s.query(model.User).filter_by(username = escape(session['username']))
           r = res[0]
           r.password = request.form['password']
           s.commit()
        return render_template('csrf.html', i=escape(session['username']))


@app.route('/logout')
@login_required
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))
        

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)