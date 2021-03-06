from flask import Flask
from flask import render_template
from flask import g
import os
import sqlite3
from datetime import datetime

from downloader.controller import DownloaderController
from saver.saver import Saver

DATABASE = os.path.join(os.path.dirname(__file__), '..', 'freelancers_friend.db')

app = Flask(__name__)
app.debug = True


@app.route('/')
@app.route('/offer/<id>')
def list(id=None):
    if can_download():
        download_offers()

    offers = get_offers_from_db()
    return render_template('list.html', offers=offers)


def download_offers():
    downloader_ctrl = DownloaderController()
    saver = Saver()
    offers = downloader_ctrl.get_offers()
    saver.save_offers(offers)


def can_download():
    conn = get_conn()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    sqlx = "SELECT datetime(timestamp, 'localtime') FROM imports ORDER BY timestamp DESC limit 1"
    cur.execute(sqlx)
    last_import = cur.fetchone()

    if last_import:
        last_timestamp = last_import[0]
        diff = datetime.now() - datetime.strptime(last_timestamp, "%Y-%m-%d %H:%M:%S")
        diff_minutes = (diff.seconds/60)
        return (diff_minutes > 15)
    else:
        return True


def get_offers_from_db():
    conn = get_conn()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    # there is a limit to 100 - i'm not interested in older offers
    sqlx = """SELECT id, title, description, source, datetime(added, 'localtime') as add_date, url,
              (strftime('%s', 'now') - strftime('%s', added))/60  <= 15 as new_offer
              FROM offers ORDER BY added desc limit 100"""
    cur.execute(sqlx)
    offers = []
    for row in cur.fetchall():
        offer = dict(row)
        add_date = datetime.strptime(offer['add_date'], "%Y-%m-%d %H:%M:%S")
        days_diff = (datetime.now()-add_date).days
        if not days_diff:
            offer['add_date'] = add_date.strftime("%H:%M")
            offer['today'] = True
        else:
            offer['add_date'] = add_date.strftime("%H:%M %d.%m")
            offer['today'] = False

        offers.append(offer)

    return offers


############
#
# simple SQLite3 management
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
