import MySQLdb
import MySQLdb.cursors


class DB:
    conn = False
    connInsert = False

    def __init__(self):
        pass

    def getConnection(self):
        self.conn = MySQLdb.connect('localhost', 'root', 'root',
                                    'wkamel_dps',
                                    cursorclass=MySQLdb.cursors.DictCursor)

    @staticmethod
    def getConnectionInsert():
        if not DB.connInsert:
            DB.connInsert = (
                MySQLdb.connect('localhost', 'root', 'root',
                                'wkamel_dps',
                                cursorclass=MySQLdb.cursors.DictCursor))
        return DB.connInsert

    def closeConnection(self):
        self.conn.close()

    def db_execute_query(self, sqlx, params=dict()):
        self.getConnection()
        cursor = self.conn.cursor()
        cursor.execute(sqlx, params)
        self.conn.commit()
        self.closeConnection()
        return cursor

    def db_get_row(self, sqlx, params={}):
        c = self.db_execute_query(sqlx, params)
        ret = c.fetchone()
        return ret

    def db_get_rows(self, sqlx):
        c = self.db_execute_query(sqlx)
        ret = c.fetchall()
        return ret
