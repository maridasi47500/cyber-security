import sqlite3
from sqlite3 import Error

class Db():
  db=r"./pythonsqlite.db"
  def get_db():
      return self.db
  def create_connection(self,db_file):
      """ create a database connection to a SQLite database """
      conn = None
      try:
          conn = sqlite3.connect(db_file)
          print(sqlite3.version)
      except Error as e:
          print(e)
      finally:
          if conn:
              conn.close()
  def create_table(self,conn, create_table_sql):
      """ create a table from the create_table_sql statement
      :param conn: Connection object
      :param create_table_sql: a CREATE TABLE statement
      :return:
      """
      try:
          c = conn.cursor()
          c.execute(create_table_sql)
      except Error as e:
          print(e)
  def get_sum(self,x):
      """
      Create a new project into the projects table
      :param conn:
      :param project:
      :return: project id
      """
      try:
        sql = ''' select sum(case when price is not null then price else 0 end) as mysum from items group by date having date = ?'''
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()
        cur.row_factory = sqlite3.Row
        myval=None
        if x:
          cur.execute(sql,(str(x),))
          conn.commit()
          myitems= cur.fetchone()
          myval=myitems["mysum"]
        else:
          myval=0
        if not myval:
          myval=0

      except Error as e:
        print(e)
        myval="0"
      finally:
        if conn:
          conn.close()
        return str(myval) if myval is not None else "0"
  def get_dates(self):
      """
      Create a new project into the projects table
      :param conn:
      :param project:
      :return: project id
      """
      try:
        sql = ''' select date from items group by date'''
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()
        cur.row_factory = sqlite3.Row
        cur.execute(sql)
        conn.commit()
        myitems= cur.fetchall()
      except Error as e:
        print(e)
        myitems= []
      finally:
          if conn:
              conn.close()
          return myitems
  def get_items(self):
      """
      Create a new project into the projects table
      :param conn:
      :param project:
      :return: project id
      """
      try:
        sql = ''' select * from items'''
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()
        cur.row_factory = sqlite3.Row
        cur.execute(sql)
        conn.commit()
        myitems= cur.fetchall()
      except Error as e:
        print(e)
        myitems= []
      finally:
          if conn:
              conn.close()
          return myitems
  def get_othermusicalinstruments(self):
      """
      Create a new project into the projects table
      :param conn:
      :param project:
      :return: project id
      """
      try:
        sql = ''' select * from musicalinstruments '''
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()
        cur.row_factory = sqlite3.Row
        cur.execute(sql)
        conn.commit()
        return cur.fetchall()
      except Error as e:
        print(e)
        return []
      finally:
          if conn:
              conn.close()
  def get_musicalinstruments(self):
      """
      Create a new project into the projects table
      :param conn:
      :param project:
      :return: project id
      """
      try:
        sql = ''' select musicalinstruments.name, notes.frequency, notes.note from musicalinstruments left join notes on notes.musicalinstrument_id = musicalinstruments.id '''
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()
        cur.row_factory = sqlite3.Row
        cur.execute(sql)
        conn.commit()
        return cur.fetchall()
      except Error as e:
        print(e)
        return []
      finally:
          if conn:
              conn.close()
  def find_user(self,project):
      """
      Create a new project into the projects table
      :param conn:
      :param project:
      :return: project id
      """
      try:
        sql = ''' select * from  users where email = ? and password = ?
                   '''
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()
        cur.row_factory = sqlite3.Row
        cur.execute(sql, project)
        conn.commit()
        x= cur.fetchone()
        print(x)
        return x
        
      except Error as e:
        print(e)
        return []
      finally:
          if conn:
              conn.close()
  def create_user(self,project):
      """
      Create a new project into the projects table
      :param conn:
      :param project:
      :return: project id
      """
      try:
        sql = ''' INSERT OR IGNORE INTO users (prenom,nom,datenaissance,genre,email,password)
                  VALUES(?,?,?,?,?,?) '''
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()
        cur.execute(sql, project)
        conn.commit()
        return cur.fetchone()
      except Error as e:
        print(e)
        return []
      finally:
          if conn:
              conn.close()
  def createitem(self,project):
      """
      Create a new project into the projects table
      :param conn:
      :param project:
      :return: project id
      """
      try:
        sql = ''' INSERT OR IGNORE INTO items(name,image, price,date)
                  VALUES(?,?,?,?) '''
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()
        cur.execute(sql, project)
        conn.commit()
        aa= cur.lastrowid
      except Error as e:
        print(e)
        aa= None
      finally:
          if conn:
              conn.close()
          return aa
  def __init__(self):


    sql1 = """ CREATE TABLE IF NOT EXISTS items (
                                        id integer PRIMARY KEY autoincrement,
                                        name text NOT NULL,
                                        image text NOT NULL,
                                        price float NOT NULL,
                                        date date NOT NULL 
                                    ); """
    sql2 = """ CREATE TABLE IF NOT EXISTS users (
                                        id integer PRIMARY KEY autoincrement,
                                        prenom text NOT NULL,
                                        nom text NOT NULL,
                                        datenaissance date NOT NULL,
                                        genre string NOT NULL,
                                        email string NOT NULL,
                                        password string NOT NULL 
                                    ); """

    self.create_connection(self.db)
    conn = sqlite3.connect(self.db)
    if conn is not None:
        self.create_table(conn,sql1)
        self.create_table(conn,sql2)
        print("key")
        if conn:
            conn.close()
    else:
        print("error crete table")

