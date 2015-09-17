from flask import Flask
from flask import render_template
from flask import g
import os
import sqlite3

DATABASE = os.path.join(os.path.dirname(__file__), '..', 'freelancers_friend.db')

app = Flask(__name__)
app.debug = True


@app.route('/')
@app.route('/offer/<id>')
def list(id=None):
    offers = get_offers_from_db()
    return render_template('list.html', offers=offers)


def get_offers_from_db():
    conn = get_conn()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    sqlx = "SELECT * FROM offers ORDER BY added desc"
    cur.execute(sqlx)
    return cur.fetchall()


############
#
# SQLite3 management
#
###########


def get_conn():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = connect_to_database()
        return db


def connect_to_database():
        return sqlite3.connect(DATABASE)


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == "__main__":
    app.run()
