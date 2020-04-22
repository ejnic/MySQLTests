import pandas as pd
import connection as con
from pandas import ExcelWriter
from pandas import ExcelFile

import mysql.connector

try:
  cnx = mysql.connector.connect(user=con.user, password=con.password, host='127.0.0.1', database=con.schema)
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cnx.close()