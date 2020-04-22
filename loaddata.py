import pandas as pd
from sqlalchemy import create_engine
import pymysql
import connection as con

class FileLoad:
    def __init__(self, filename, filepath, tablename, schema, constring):
        self.filename = filename
        self.filepath = filepath
        self.tablename = tablename
        self.schema = schema
        self.constring = constring

    def DoLoad(self):
        self.cleanedname = re.sub( r'[^\x00-\x7F]+', '', self.cleanedname)

        sqlengine = create_engine(self.constring, pool_recycle=3600)
        dbconnection = sqlengine.connect()

        frame = dataFrame.to_sql(self.tablename, dbconnection, if_exists='fail');