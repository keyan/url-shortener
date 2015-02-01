from itertools import count
import sqlite3
from contextlib import closing
from flask import Flask, render_template, request, redirect, session, g, \
     abort, flash, url_for

# Configuration
DATABASE = 'shorten.db'
DEBUG = True
SECRET_KEY = 'dev'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        short_url = id_gen.next()
        g.db.execute('INSERT INTO urls VALUES (?, ?)',
                     (short_url,
                      request.form['original_url']))
        g.db.commit()
        short_url = "http://shortenr.herokuapp.com/" + str(short_url)
        # short_url = "http://127.0.0.1:5000/" + str(short_url)
        return render_template("index.html", short_url=short_url)
    return render_template("index.html")


@app.route("/<int:redirect_id>")
def shorten(redirect_id):
    cur = g.db.execute('SELECT original_url \
                        FROM urls \
                        WHERE url_id=:id', {"id": redirect_id})
    orig_url = cur.fetchall()
    redirection = 'http://' + str(''.join(orig_url[0]))
    return redirect(redirection)


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


if __name__ == "__main__":
    id_gen = count(1, 1)
    app.run()
