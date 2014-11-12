import sqlalchemy
import urllib
import azurecfg

from sqlalchemy import *

dbconn = "DRIVER={{FreeTDS}};Server={};Database=atdblasphemy;UID={};PWD={};TDS_Version=7.1;Port=1433;".format(
    azurecfg.sql['server'], azurecfg.sql['uid'], azurecfg.sql['pwd']
)

quoted = urllib.quote_plus(dbconn)
engine = sqlalchemy.create_engine('mssql+pyodbc:///?odbc_connect={}'.format(quoted))
dbconn = engine.connect()

metadata = MetaData()
metadata.reflect(engine)

products = metadata.tables['Products']
