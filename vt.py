import sqlite3 as sql

class vt():
    def __init__(self):
        self.con = sql.connect('upwork.sqlite', check_same_thread=False)
        self.cur = self.con.cursor()


    def Create_table(self):
        vt_table = """CREATE TABLE IF NOT EXISTS job (id INTEGER PRIMARY KEY,title, content,published,link,add_date,send VARCHAR(1))"""
        vt_table2 = """CREATE TABLE IF NOT EXISTS rss (id INTEGER PRIMARY KEY,link,add_date)"""
        vt_table3 = """CREATE TABLE IF NOT EXISTS log (id INTEGER PRIMARY KEY,title,content,log_date)"""
        vt_table4 = """CREATE TABLE IF NOT EXISTS note (id INTEGER PRIMARY KEY,title,content,add_date)"""
        self.cur.execute(vt_table)
        self.cur.execute(vt_table2)
        self.cur.execute(vt_table3)
        self.cur.execute(vt_table4)


    def add_rss(self,link):
        value = ("""INSERT INTO rss(id,link,add_date) VALUES (NULL,?,datetime('now','localtime'))""")
        self.cur.execute(value,[link])
        self.con.commit()

    def addnote(self,title,content):
        value = ("""INSERT INTO note(id,title,content,add_date) VALUES (NULL,?,?,datetime('now','localtime'))""")
        self.cur.execute(value, [title, content])
        self.con.commit()


    def shownote(self):
        self.cur.execute("""SELECT id,content FROM note""")
        data = self.cur.fetchall()
        return data

    def into_data(self,title,content,published,link):
        value = """INSERT INTO job(id,title, content, published,link,add_date,send) VALUES(NULL,?,?,?,?,datetime('now','localtime'),'0') """
        self.cur.execute(value,[title,content,published,link])
        self.con.commit()


    def take_data_all(self,data):
        self.cur.execute("""SELECT * FROM {}""".format(data))
        data = self.cur.fetchall()
        return data

    def vt_title(self,data):
        self.cur.execute("""SELECT title FROM {}""".format(data))
        data = self.cur.fetchall()
        return data

    def search_id(self,id):
        self.cur.execute("""SELECT * FROM job WHERE id='{}'""".format(id))
        data = self.cur.fetchall()
        return data


    def filter(self,veri):
        self.cur.execute("""SELECT * FROM job WHERE link='{}'""".format(veri))
        if self.cur.fetchall():
            return True
        else:
            return False

    def write_log(self,title,content):
        value = """INSERT INTO log(id,title,content,log_date) VALUES(NULL,?,?,datetime('now','localtime')) """
        self.cur.execute(value, [title, content])
        self.con.commit()

    def fetch_data(self):
        value = """SELECT * FROM job WHERE send='0'"""
        self.cur.execute(value)
        count = self.cur.fetchall()
        return count

    def change(self,id):
        value = """UPDATE job SET send = 1 where id ='{}'""".format(id)
        self.cur.execute(value)
        self.con.commit()


    def check_rss(self):
        self.cur.execute("""SELECT id FROM rss """)
        if self.cur.fetchall():
            return True
        else:
            return False

    def fetch_note(self):
        self.cur.execute("""SELECT id FROM note """)
        return self.cur.fetchall()


    def deljob(self):
        value = """DELETE FROM job"""
        self.cur.execute(value)
        self.con.commit()

    def read_log(self,limit):
        self.cur.execute("""SELECT * FROM log ORDER BY id DESC LIMIT '{}'""".format(limit))
        data = self.cur.fetchall()
        return data
