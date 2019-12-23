 # this code is to read Excel file and load to SQL tables

 # Change file directory for Excel file
import os

os.chdir (r'C:\Users\Mei\Desktop\DP\XZhang\Python')
cwd = os.getcwd()

 # print current dirsctory
print('current directory is: ', cwd)

import pandas as pd
import numpy as np
import pandas.io.sql
import pymssql
import xlrd
from datetime import datetime
import pyodbc



### Uisng windows authentication.

# Use PyMSSQL module for conection: THere is issue for this connetion method

#conn=pymssql.connect(server='HP1\SQLEXPRESS', database='XZ')


# Use PyODBC to establish connection

conn = pyodbc.connect(
    Driver = 'SQL Server',
    Server = 'HP1\SQLEXPRESS',
    Database = 'XZ',
    Trusted_Connection = 'yes'
    )

# Define a method for cursor
cur =conn.cursor()

# read EXCEL source data

book = xlrd.open_workbook('Emp.xlsx')
sheet =book.sheet_by_name('Sheet1')

# Empty stage table
cur.execute('truncate table [XZ].[dbo].[Emp_stage]')
cur.commit()

print ('Stage table truncated')

query = """  insert into [XZ].[dbo].[Emp_stage]
        (Emp_ID
      ,FRST_NM
      ,LAST_NM
      , DOB
      ,Salary
      ,Title)
    values (?,?,?,?,?, ?); """

#Insert each row into table
for r in range(1, sheet.nrows):
    Emp_ID = sheet.cell(r,0).value
    FRST_NM = sheet.cell(r,1).value
    LAST_NM = sheet.cell(r,2).value
    DOB = sheet.cell(r,3).value
    Salary    = sheet.cell(r,4).value if sheet.cell(r,4).value !='' else 0
    Title = sheet.cell(r,5).value

    values =(Emp_ID,FRST_NM, LAST_NM, DOB, Salary,Title )

    cur.execute(query,  values)

    cur.commit()

# Validate rows were inderted

cur.execute('select  * from [XZ].[dbo].[Emp_stage]')
rows =cur.fetchall()

print('records from source table\n') 

for row in rows:
    print(row)
##numrows = int(cur.rowcount)
##print ('Rows to be inserted: ', numrows)

# Empty final table

cur.execute('truncate table [XZ].[dbo].[Emp] ')
cur.commit()

# ETL data from staging table to final table

query = """insert into [XZ].[dbo].[Emp] ([Emp_ID]
      ,[FRST_NM]
      ,[LAST_NM]
      ,[Salary]
      ,[Title])
     SELECT TOP (1000) [Emp_ID]
      ,lower([FRST_NM])
      ,upper([LAST_NM])
      ,cast([Salary] as INT)
      ,[Title]
  FROM [XZ].[dbo].[Emp_stage]"""

cur.execute(query)

cur.commit()

# Get number of records inserted

cur.execute('select * from [XZ].[dbo].[Emp]')
rows=cur.fetchall()

print('\nThese are records from final table\n')

for row in rows:
    print(row)

numrows = int(cur.rowcount)
print(numrows)

print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
  

cur.close()


                     
