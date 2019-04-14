# LOAD LIBRARIES_____________________________________________________________
import pandas as pd
import nltk
import string
import os
import mysql.connector

# LOAD MODULES

import module3_token_freq_by_label as m3



# CONNECTION________________________________________________________________
mydb = mysql.connector.connect(
        host="localhost",
        user="ccirelli2",
        passwd="Work4starr",
        database='GSU'
        )
mycursor = mydb.cursor()



def get_table_data(mydb, col, threshold):

    sql_command = '''SELECT *
                     FROM DL_2019_PROJ_A_TOKENS2
                     WHERE {} > {};'''.format(col, threshold)

    df = pd.read_sql(sql_command, mydb)
    return df

def insert_token_delta(mydb, mycursor, col, delta, token):

    sql_command = '''UPDATE DL_2019_PROJ_A_DELTAS 
                     SET %s = %s
                     WHERE TOKEN = %s;
                     '''
    val = (col, delta, token)
    # The first {} is column and the second {} would be the freq
    mycursor.execute(sql_command, val)
    mydb.commit()





