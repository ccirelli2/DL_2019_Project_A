# TEXT PROCESSING 
'''
1.)  Concatenate Text 
2.)  Clean
3.)  Create frequency table
4.)  Vectorize rows using frequency table. 
'''

### Import Libraries
import os
import pandas as pd
import nltk
import string

### Import Modules
import module2 as m1

# Load Dataset
def get_df_file():
    target_dir = r'/home/ccirelli2/Desktop/GSU/2019_Spring/Deep_Learning_Spring_2019/Project_A'
    os.chdir(target_dir)
    df = pd.read_excel('ID_text_table.xlsx')
    df_tranpose = df.transpose()
    return df_transpose


### Clean Text
# Read back in concatenated text
#concat_text = open('concat_text.txt').read()

### Run Text Through Cleaning Pipeline, Rejoin tokens to string
#concat_text_clean = ' '.join(m1.clean_and_tokenize_text(concat_text))

### Write Back to Text File (Purpose:  Ability to work on clean text withouth runing pipeline again)
#m1.create_text_file('cleaned_text.txt', concat_text_clean)


# Get Frequency of Words In Text
'''
cleaned_text_cleaned = open('cleaned_text.txt').read()
df_token_freq_table = m1.create_word_freq_table(cleaned_text_cleaned)
df_token_freq_table.to_excel('token_freq_table.xlsx')
'''

# Read Back In Freq Table
df_freq_table = pd.read_excel('token_freq_table.xlsx')
print(df_freq_table.head())











