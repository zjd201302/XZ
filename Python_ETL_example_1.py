## use python to load Excel file to SQL Server table and archive file

## check whether the file exists

import os

## Change CWD

os.chdir ('C:\\Users\\Mei\\Desktop\\DP\\XZhang\\Python\\Data_Src')

cwd = os.getcwd()

 # print current dirsctory
print('current directory is: ', cwd)



##file_path = 'C:\\Users\\Mei\\Desktop\\DP\\XZhang\\Python\\Data_Src\\Questionaire.xlsx'
file_path = 'Questionaire.xlsx'

archive_path = 'C:\\Users\\Mei\\Desktop\\DP\\XZhang\\Python\\Data_Dest\\Questionaire.xlsx' 


if os.path.exists(file_path):
    print ("FOUND expected file and this is file path: {}".format(file_path))
    pass
else:
    print ("Expected file does not exist. please check file path: {} ".format(file_path))




## Establish connection to SQL Server using pyodbc module

import pyodbc


conn = pyodbc.connect(
    Driver = 'SQL Server',
    Server = 'HP1\SQLEXPRESS',
    Database = 'XZ',
    Trusted_Connection = 'yes'
    )

print ('Connection to SQL Server established')

## Define a method for cursor
cur = conn.cursor()


## Use xlrd module to read Excel file

import xlrd

# read EXCEL source data

book = xlrd.open_workbook('Questionaire.xlsx')
sheet =book.sheet_by_name('Questionaire')

print ('Source Excel work sheet read.....')

print ('Empty staging table ....')


cur.execute('truncate table Questionaire_stg')
cur.commit()

## Load raw data from source Excel to SQL Server Stage table

print ('Loading staging table ...')

query = """  insert into [XZ].[dbo].[Questionaire_stg]
        (Question
      ,Answer)
    values (?,?); """


#Insert each row into table
for r in range(3, sheet.nrows):
    Question = sheet.cell(r,0).value
    Answer = sheet.cell(r,1).value


    values =(Question,Answer)

    cur.execute(query,  values)

    cur.commit()


print ('Staging table loaded...')

## Pivot the raw and Load it to final table


query_load = """
insert into XZ.dbo.Questionaire (Provider, Eff_DT, TIN_1, Tin_2, Certificate, Care_plan, Clinical_Path_Way) 
select  Provider, Efftive_Date, TIN_1, TIN_2, Certificate, Care_Plan, Cinical_Pathway
 from XZ.dbo.Questionaire_stg
 pivot
 (max(answer) for question in (Provider, Efftive_Date, TIN_1, TIN_2, Certificate, Care_Plan, Cinical_Pathway
)
 ) pivotTable

"""

cur.execute(query_load)

cur.commit()

print ('Raw data was pivoted and loaded into destination table ...')

## Archive file and append timestamp to file name

import shutil
shutil.move(file_path, archive_path)

print ('Source Excel file was moved to archive folder ...')

