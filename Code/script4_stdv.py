# SCRIPT 4 - CALCULATE STANDARD DEVIATION FROM OTHER LABELS


# LOAD LIBRARIES_____________________________________________________________
import pandas as pd
import nltk
import string
import os
import mysql.connector
import numpy as np

# LOAD MODULES

import module3_token_freq_by_label as m3
import module4_get_stdv as m4


# CONNECTION________________________________________________________________
mydb = mysql.connector.connect(
        host="localhost",
        user="ccirelli2",
        passwd="Work4starr",
        database='GSU'
        )
mycursor = mydb.cursor()

def driver_function(mydb):
    
    # Get Table Data
    '''Will be a unique table on each iteration'''
    table_data = m4.get_table_data(mydb, '0_', .25) 

    # Get Difference for Col 0 vs Others
    for row in table_data.itertuples():
        avg = (row[4] + row[5] + row[6] + row[7] + row[8] + row[9] + row[10]) / 7
        ratio = round(row[3] / avg, 2)

        # Insert Ratio Into Table
        try:
            if ratio is None:
                m4.insert_token_delta(mydb, mycursor, '0_', row[3], row[2])
                #print('Ratio is None {}'.format(row[3]))
            else:
                m4.insert_token_delta(mydb, mycursor, '0_', ratio, row[2])
                #print('Inserting ratio {}'.format(ratio))
        except mysql.connector.errors.DataError:
            print('Data error')

        #except mysql.connector.errors.ProgrammingError:
        #    print('Programming Error')

driver_function(mydb)







    




