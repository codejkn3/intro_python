import mysql.connector
from mysql.connector import errorcode

try:
  cnx = mysql.connector.connect(host='novoxen1',user='jnealy', password='sigmajkn3', database='test')

  cur = cnx.cursor()
  query = ("show tables")
  cur.execute(query)
  rows = cur.fetchall()
  for row in rows:
      print (row)
      
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong your username or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exists")
  else:
    print(err)
else:
  cnx.close()
