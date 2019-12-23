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
##import xlrd
from datetime import datetime
import pyodbc
import getpass   # for reading password
import time

##p=getpass.getpass(); # ask for user password

t0= time.time()   # get current time

conn = pymssql.connect(host= 'HP1\SQLEXPRESS',
                       database='XZ',
                       user = 'HP1\Mei',
                       password = 'p')
