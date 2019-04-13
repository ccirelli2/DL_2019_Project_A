
# IMPORT LIBRARIES

import mysql.connector
import pandas as pd
import os




# CONNECTION

mydb = mysql.connector.connect(
        host="localhost",
        user="ccirelli2",
        passwd="Work4starr",
        database='GSU'
        )


mycursor = mydb.cursor()

#mycursor.execute(sql_command, (100000,1))
#mydb.commit()


# Load Data File
file_dir = '/home/ccirelli2/Desktop/GSU/2019_Spring/Deep_Learning_Spring_2019/DL_2019_Project_A/Data_files'
file_name = 'Label.xlsx'
df = pd.read_excel(file_dir + '/' + file_name)



for row in df.itertuples():
    ID = str(row[1])
    Label = str(row[2])
    sql_command = '''INSERT INTO DL_2019_PROJ_A_LABELS (ID, TEXT)
                 VALUES ({}, {})'''.format(ID, Label)
    mycursor.execute(sql_command)
    mydb.commit()




