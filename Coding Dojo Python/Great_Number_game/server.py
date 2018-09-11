from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes

import random

@app.route('/')
def index():
    session['guess'] = 0
    session['curr_random'] = 0
    session.pop('guess')
    session.pop('curr_random')
    session['curr_random'] = random.randint(1, 100)
    print  session['curr_random']
    return render_template("index.html")

@app.route('/returnguess', methods=['POST'])
def returnguess():
    print  request.form['guess']
    session['guess'] = int(request.form['guess'])
    return render_template("result.html")

@app.route('/correctguess', methods=['POST'])
def correctguess():
    return redirect('/')

app.run(debug=True) # run our server