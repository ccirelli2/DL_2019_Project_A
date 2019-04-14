
# IMPORT LIBRARIES
import mysql.connector
import pandas as pd
import string
import nltk
import os




# CONNECTION
mydb = mysql.connector.connect(
        host="localhost",
        user="ccirelli2",
        passwd="Work4starr",
        database='GSU'
        )

mycursor = mydb.cursor()

# File Dir
file_dir = '/home/ccirelli2/Desktop/GSU/2019_Spring/Deep_Learning_Spring_2019/DL_2019_Project_A/Data_files'


# CREATE TABLE WITH LABELS-------------------------------------------------

def create_table_labels(mycursor, file_dir):
    file_name = 'Label.xlsx'
    df = pd.read_excel(file_dir + '/' + file_name)


    for row in df.itertuples():
        ID = str(row[1])
        Label = str(row[2])
        sql_command = '''INSERT INTO DL_2019_PROJ_A_LABELS (ID, TEXT)
                 VALUES ({}, {})'''.format(ID, Label)
        mycursor.execute(sql_command)
        mydb.commit()
    
    return None


# CREATE TABLE WITH TEXT--------------------------------------------------------

def clean_text(text):
   
    Punct_list = set([punct for punct in string.punctuation])
    Text_tokenized = nltk.word_tokenize(text)
    Filter_isalpha = filter(lambda x: x.isalpha(), Text_tokenized)
    Filter_punct   = filter(lambda x: (x not in Punct_list), Filter_isalpha) 
    Token_list     = list(Filter_punct)
    Return_string  = ' '.join(Token_list)
    return Return_string


def create_table_text(mydb, mycursor, file_dir):
    file_name = 'Patent_ID_Plus_Text.xlsx'
    df = pd.read_excel(file_dir + '/' + file_name)

    for row in df.itertuples():
        try:
            ID = str(row[1])
            Text = str(row[2])
            Text_clean = clean_text(Text)

            sql_command = '''INSERT INTO DL_2019_PROJ_A_TEXT (ID, TEXT)
                         VALUES (%s, %s)'''
            val = (ID, Text_clean)
            mycursor.execute(sql_command, val)
            mydb.commit()
        except mysql.connector.errors.DatabaseError: 
            print('error')
    return None


def create_token_table(mydb, mycursor, file_dir):
    file_name = 'Word_freq_table.xlsx'
    df = pd.read_excel(file_dir + '/' + file_name)
    df_list = list(df.index)
    
    Count = 0
    
    for token in df_list:
        try:
            sql_command = '''INSERT INTO DL_2019_PROJ_A_TOKENS (PKEY, TOKEN)
                         VALUES ('{}', '{}')'''.format(Count, token)
            mycursor.execute(sql_command)
            mydb.commit()
            Count += 1
        except mysql.connector.errors.DatabaseError:
            print('insert error')
    return None























