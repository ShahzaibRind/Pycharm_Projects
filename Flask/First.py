from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/harry")
def harry():
    name1 = "harry"
    return render_template('about.html', name2 = name1)


@app.route("/bootstrap")
def bootstrap():
    return render_template('bootstrap.html')

app.run()