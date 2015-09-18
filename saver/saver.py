import sqlite3
import os

DATABASE = os.path.join(os.path.dirname(__file__), '..', 'freelancers_friend.db')


class Saver(object):
    """ Class for persising offers in database """
    _database = None

    def save_offers(self, offers):
        conn = self.get_db()
        cur = conn.cursor()
        for o in offers:
            sqlx = """INSERT INTO offers(id, title, description, url, source)
                    VALUES(
                       ?, ?, ?, ?, ?
                    ) """

            try:
                cur.execute(sqlx, (
                    o.id, o.title, o.description, o.url, o.source
                ))
                conn.commit()
            except Exception as Ex:
                print "This offer already exists in DB, %s %s" % (o.id, o.title)

        self.add_inport_info()

    def add_inport_info(self):
        conn = self.get_db()
        cur = conn.cursor()
        sqlx = "INSERT INTO imports VALUES(DATETIME('now'))"
        cur.execute(sqlx)
        conn.commit()

    def get_db(self):

        db = getattr(self, '_database', None)
        if db is None:
            db = self._database = self.connect_to_database()

        return db

    def connect_to_database(self):
            return sqlite3.connect(DATABASE)
