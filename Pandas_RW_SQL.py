# Pandas read write to SQL

import pandas as pd
import sqlalchemy
import pymysql
import pyodbc
import urllib

# Create engine to connect to SQL server
cc = r'Driver={SQL Server}; Server=HP1\SQLEXPRESS; Database=XZ; Trusted_Connection=True;'

##conn = pyodbc.connect(cc)
params =urllib.parse.quote_plus(cc);

engine = sqlalchemy.create_engine("mysql+pymysql:///?odbc_connect=%s" % params)

df=pd.read_sql_table('Emp', engine)
print(df)
