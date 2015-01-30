import random
from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form['original_url']
        short_url = int(random.getrandbits(16))
        url_list[short_url] = original_url
        short_url = "http://127.0.0.1:5000/" + str(short_url)
        return render_template("index.html", short_url=short_url)
    return render_template("index.html")


@app.route("/<int:redirect_url>")
def shorten(redirect_url):
    redirection = 'http://' + url_list[redirect_url]
    return redirect(redirection)


def uniqueid():
    for i in xrange(100000):
        yield i


if __name__ == "__main__":
    url_list = {}
    app.run(debug=True)
