# FUNCTIONS ASSOCIATED WITH SCRIPT 3 - TOKEN FREQUENCY BY LABLE



# LOAD LIBRARIES_____________________________________________________________
import pandas as pd
import nltk
import string
import os
import mysql.connector



def get_text_4_specific_label(mydb, label):
    '''Retreive a dataframe of the Label + Text limited for a given Label'''
    sql_command = '''SELECT 
                   DL_2019_PROJ_A_LABELS.LABEL, 
                   DL_2019_PROJ_A_TEXT.TEXT

                 FROM GSU.DL_2019_PROJ_A_TEXT
                   
                   JOIN DL_2019_PROJ_A_LABELS ON
                        DL_2019_PROJ_A_TEXT.ID = DL_2019_PROJ_A_LABELS.ID    
                   WHERE LABEL = '{}';'''.format(label)
    df = pd.read_sql(sql_command, mydb)
    return df

def get_token_table(mydb):
    sql_command = '''SELECT TOKEN
                     FROM DL_2019_PROJ_A_TOKENS2;'''
    df = pd.read_sql(sql_command, mydb)
    return df

def insert_token_freq(mydb, mycursor, col, token_freq, token):

    sql_command = '''UPDATE DL_2019_PROJ_A_TOKENS2 
                     SET {} = {}
                     WHERE TOKEN = '{}';
                     '''.format(col, token_freq, token)
    # The first {} is column and the second {} would be the freq
    mycursor.execute(sql_command)
    mydb.commit()

def get_table_col_names(mydb):

    sql_command = '''SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS 
                     WHERE TABLE_SCHEMA = 'GSU' AND TABLE_NAME = 'DL_2019_PROJ_A_TOKENS2' '''

    df = pd.read_sql(sql_command, mydb)
    # Index 2: so that we don't include the PKEY nor Token
    return df[2:]






