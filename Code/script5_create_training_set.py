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
import module0_utility_functions as m0


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
token_file_v2 = 'Tokens_trainingset_v2.xlsx'

# Retreive List Tokens
df_tokens = pd.read_excel(data_dir + '/' + token_file_v2)
list_tokens = [x for x in df_tokens['TOKENS']]

# Retreive Text + Lables
df_entire_dataset = m3.get_entire_dataset(mydb)
df_entire_dataset_limited = df_entire_dataset.head()



# Define Function Vectorize Text:
def vectorize_text(list_tokens, df_entire_dataset):

    # Create & Dataframe to house the vectors
    df = pd.DataFrame({}, index = [x for x in list_tokens])

    # Iterate over Dataframe w/ Text:
    for row in df_entire_dataset.itertuples():

        # Process Text:
        clean_tokenized_text = m1.clean_and_tokenize_text(row[2])

        # For Each Row we are going to build a list
        list_matches = []

        # Iterate List of Tokens
        for token in list_tokens:
            if token in clean_tokenized_text:
                list_matches.append(1)
            else:
                list_matches.append(0)

        # Once We are Finished Building Our List, we need to add it to our dataframe as a col.
        df[row[0]] = list_matches    # row[0] is the index, so we will need to add column names 
                                     # afterwards. 
        
        # Provide Update
        print('Vectorization completed for row {}'.format(row[0]))
    
    print('Process complete.  File written to hard drive')

    return df


df_output = vectorize_text(list_tokens, df_entire_dataset)
df_transpose = df_output.transpose()
df_transpose['LABEL'] = df_entire_dataset['LABEL']



# Chose Location to write file
m0.write_to_excel(df_df_transpose, 'Second_file', target_dir)








