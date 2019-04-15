# DRIVER FUNCTION - DATA PREPARATION


### Import Libraries-------------------------------------------------------------
import os
import re
import nltk
import pandas as pd


### Import File  **You need to change this to the dir on your computer***
target_dir = r'/home/ccirelli2/Desktop/GSU/2019_Spring/Deep_Learning_Spring_2019/DL_2019_Project_A/Data_files'
os.chdir(target_dir)
original_file = 'train.txt'

### Import Module 
import module1_proj_A as m1

### Create File Excluding non-utf8 characters

def driver_funct_text_prep(Original_text_file, target_dir):

    # Step 1:  Clean Text of Non-utf8 values
    '''cleans text and writes file back target_dir'''
    m1.get_clean_file_utf8(Original_text_file, 'clean_txt1_utf8.txt', target_dir)
    
    # Step 2: Create Dataframe (Key = Patent ID, Value = Text)
    clean_text_file = open('clean_txt1_utf8.txt').read()
    m1.create_df_ID_text(clean_text_file, 'Patent_ID_Text_Table.xlsx', target_dir)

    # Step 3:  Create Concatenated Text File From Patent ID Table
    df_patentID_table = m1.load_Patent_ID_table('Patent_ID_Text_Table.xlsx')
    m1.create_concat_txt_file_from_df(df_patentID_table, 'Concat_txt_file_dirty.txt', target_dir)

    # Step 4: Run Text Through Cleaning Pipeline
    concat_text_dirty = open('Concat_txt_file_dirty.txt').read()
    concat_text_clean = ' '.join(m1.clean_and_tokenize_text(concat_text_dirty))
    m1.create_text_file(concat_text_clean, 'cleaned_text.txt', target_dir)
    
    # Step 5:  Create Word Freq Table
    cleaned_text_cleaned = open('cleaned_text.txt').read()
    df_freq_table = m1.create_word_freq_table(cleaned_text_cleaned, 'Word_Freq.xlsx', target_dir)    
    return df_freq_table






def get_word_freq_by_stage():

    # Change to Data Dir
    os.chdir('/home/ccirelli2/Desktop/GSU/2019_Spring/Deep_Learning_Spring_2019/DL_2019_Project_A/Data_files')


    # Step1:  Load Text File
    text_file_tokens = open('cleaned_text.txt').read()

    # Step2:  Tokenize Text of Stem Words
    tokens_stem_words = nltk.word_tokenize(text_file_tokens)

    # Merge Class On Text (Excel File)    
    df_text = pd.read_excel('Patent_ID_Text_Table.xlsx')
    df_text_tp = df_text.transpose() 
    df_labels = pd.read_excel('Label.xlsx')
    df_merged = df_text_tp.merge(how = 'outer', df_labels, left_index = True, right_index = True)










