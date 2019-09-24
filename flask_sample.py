import random as rd

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hello')
def hello():
    return '<h1>Hello World!!!!!!!!!!</h1>'


@app.route('/goodbye')
def goodbye():
    return 'Goodbye!'


@app.route('/add/<a>/<b>/')
def add(a, b):
    return str(int(a) + int(b))


@app.route('/omikuji/')
def ViewFunction():
    kuji = ['大吉', '吉', '凶', '大凶']
    num = rd.randint(0, len(kuji) - 1)
    # return f'今日の運勢は・・・{kuji[num]}'
    result = kuji[num]
    return render_template('omikuji.html', result=result)



if __name__ == '__main__':
    app.run(debug=True, port=7777)
