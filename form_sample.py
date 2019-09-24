from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template("form.html")
    if request.method == 'POST':
        username = None
        username = request.form['username']
        return render_template("form.html", username=username)


if __name__ == '__main__':
    app.run(debug=True, port=8888)
