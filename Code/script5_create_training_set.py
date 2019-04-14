# CREATE TRAINING SET

# Import Libraries
import pandas as pd
import os
import mysql.connector
import string
import nltk

# Import Modules
import module1_proj_A as m1      # cleaning pipeline is located here
import module3_token_freq_by_label as m3  # sql code select functions here

# Establish MySQL Connection
mydb = mysql.connector.connect(
        host="localhost",
        user="ccirelli2",
        passwd="Work4starr",
        database='GSU'
        )

mycursor = mydb.cursor()

# Data files
data_dir =  r'/home/ccirelli2/Desktop/GSU/2019_Spring/Deep_Learning_Spring_2019/DL_2019_Project_A/Data_files'
token_file = 'Tokens_trainingset_04142019.xlsx'


# Retreive List Tokens
df_tokens = pd.read_excel(data_dir + '/' + token_file)
list_tokens = [x for x in df_tokens['TOKENS']]



# Retreive Text + Lables
m3.get_entire_dataset(mydb)

