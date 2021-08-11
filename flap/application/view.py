from flask import request, redirect, url_for, render_template, session, Response
from flap import app

#ここからメモを作成
@app.route('/', methods=['GET', 'POST'])
def form():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    if request.method == 'POST':
        query = request.form['query']
        suggests = request.form['suggests']

        with open('flap/application/scripts/tempo/memo.txt', "w") as f:
            f.writelines(query + '\n')
            f.writelines(suggests)

        return redirect(url_for('quux'))

    return render_template('form.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:pass
        elif request.form['password'] != app.config['PASSWORD']:pass
        else:
            session['logged_in'] = True
            return redirect(url_for('form'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect('/')
