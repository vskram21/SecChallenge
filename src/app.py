from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='')


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/serialization')
def serialization():
    return render_template('serialization.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')

@app.route('/secret')
def secret():
    return render_template('secret.html')
    # return "Congrats! You are almost there. Go to the page "

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return request.form['password']
        if (request.form['username'] == 'admin') & (request.form['password'] == '4015bc9ee91e437d90df83fb64fbbe312d9c9f05') :
            return "Welcome Admin"
    return render_template('login.html')

@app.route('/cors')
def cors():
    return render_template('cors.html')

@app.route('/4015bc9ee91e437d90df83fb64fbbe312d9c9f05', methods=['GET', 'POST'])
def directoryfound():
    if request.method == 'GET':
        return render_template('crackcode.html')
    else:
        if (request.form['pin']=='9876'):
            return render_template('success.html')
            # return "Success! You have completed the challenge!   Here is your flag 987947614649875449846516765449"
        else:
            return render_template('crackcode.html')


@app.route('/csrf')
def csrf():
    return render_template('csrf.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)