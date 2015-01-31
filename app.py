from itertools import count
import sqlite3
from flask import Flask, render_template, request, redirect, session, g, \
     abort, flash, url_for

# Configuration
DATABASE = '/database/shortener.db'
DEBUG = True
SECRET_KEY = 'dev'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form['original_url']
        short_url = id_gen.next()
        url_list[short_url] = original_url
        short_url = "http://127.0.0.1:5000/" + str(short_url)
        return render_template("index.html", short_url=short_url)
    return render_template("index.html")


@app.route("/<int:redirect_id>")
def shorten(redirect_id):
    redirection = 'http://' + url_list[redirect_id]
    return redirect(redirection)


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


if __name__ == "__main__":
    url_list = {}
    id_gen = count(1, 1)
    app.run(debug=True)
