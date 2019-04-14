# GET AVERAGE FREQUENCY OF EACH TOKEN BY LABEL

'''
Purpose:        Get the average number of times each token shows up in each label. 
                
Table1:         Tokens:  You'll need a table with rows as tokens and column as the labels. 
Table2:         Text:
Table3:         Join: the Text table and Label Table. 
                Group the text by label. 

Process:        Iterate over the text associated with each label.
                Calculate the freq as count / total len. 
                Insert this into your token table. 
                
'''

# LOAD LIBRARIES_____________________________________________________________
import pandas as pd
import nltk
import string
import os
import mysql.connector

# IMPORT MODULES____________________________________________________________
os.chdir(r'/home/ccirelli2/Desktop/GSU/2019_Spring/Deep_Learning_Spring_2019/DL_2019_Project_A/Code')
import module1_proj_A as m1
import module3_token_freq_by_label as m3


# CONNECTION________________________________________________________________
mydb = mysql.connector.connect(
        host="localhost",
        user="ccirelli2",
        passwd="Work4starr",
        database='GSU'
        )
mycursor = mydb.cursor()



# DATA_____________________________________________________________________

list_col_names = m3.get_table_col_names(mydb)['COLUMN_NAME']
list_tokens    = m3.get_token_table(mydb)['TOKEN']



# DRIVER FUNCTION_________________________________________________________

# Iterate Over List Column Names
'''
for col in list_col_names:

    print('Starting function for col {}'.format(col))

    # Get Text Associated With This Label
    label = col[:1]                                      # drops off the _ from the end 
    
    # Retreive the Text Associated With This Label
    df_text = m3.get_text_4_specific_label(mydb, label)   

    Num_tokens = len(df_text.index)
    Token_counter = 0

    # Iterate Over List Of Tokens
    for token in list_tokens:
        # Create a Counter For The Number of Rows Where Token Is Matched
        tokens_matched = 0
    
        # Iterate over each row in our df_text dataframe
        for row_text in df_text.itertuples():
            # Clean and tokenize the text in that row
            clean_tokenize_text = m1.clean_and_tokenize_text(row_text[2])
     
            # if the token is in the list of tokens add 1 to the counter. 
            if token in clean_tokenize_text:
                tokens_matched += 1
        
        # Calculate Token Freq
        token_freq = round((tokens_matched / Num_tokens * 100),2)
        print(token_freq)
        print(Num_tokens)
        # Insert Token Freq Into Database
        m3.insert_token_freq(mydb, mycursor, col, token_freq, token)
        
        # Increase Token Counter By One
        Token_counter += 1

        # Progress
        progress = round((Token_counter / Num_tokens)*100, 4)
        print('Percentage Completion for Col {} => {}%'.format(col, progress))
'''     



for col in list_col_names:

    # Update - Starting Function
    print('Starting function for col {}'.format(col))

    # Retreive the Text Associated With This Label
    label = col[:1]
    df_text = m3.get_text_4_specific_label(mydb, label)

    # Define Length of Rows
    Num_tokens = len(df_text.index)

    # Create a Dictionary for Count of Matched Tokens
    Dict_matched_tokens = {}

    for row_text in df_text.itertuples():
        clean_tokenize_text = m1.clean_and_tokenize_text(row_text[2])

        for token in list_tokens:
            if token in clean_tokenize_text:
                Dict_matched_tokens[token] = Dict_matched_tokens.get(token, 0) + 1

    # Update- Completion Dict
    print('Dictionary completed for col {}'.format(col))

    # Insert Token Freq Into Database
    for token in Dict_matched_tokens:
        token_freq =  round((Dict_matched_tokens[token] / Num_tokens),2)

        # Insert
        m3.insert_token_freq(mydb, mycursor, col, token_freq, token)

    # Update - Completion of Col
    print('Insertion completed for col {}\n'.format(col))





















































