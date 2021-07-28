import sqlite3
from flask import Flask, render_template

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def render_index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)


@app.route('/render_beers')
def render_beers():
    return render_template('beers.html')


@app.route('/render_about')
def render_about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()
