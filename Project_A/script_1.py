# SCRIPT1 - PROCESS TEXT



### Import Libraries
import os
import re
import nltk
import pandas as pd


### Import File
target_dir = r'/home/ccirelli2/Desktop/GSU/2019_Spring/Deep_Learning_Spring_2019/Project_A'
original_file = 'train.txt'

### Import Module 
import module_1 as m1

### Create File Excluding non-utf8 characters
#m1.get_clean_file_utf8(original_file)


### Separate Identifier Code From Text
clean_text_file = open('train_clean.txt').read()

### Find All Patent Numbers
# Define Regex Expression
regex = re.compile('[0-9]{11}')
# Get All Matches - Return Iterator
re_search = re.finditer(regex, clean_text_file)

# Create DataFrame to Capture Identifer + Text
df = pd.DataFrame({}, index = [0])

# Convert Iterator to List
re_results_list = [x.group() for x in re_search]


# Fuction Splits On First & Second Match to Isolate Text Associated w/ Match1


def create_df_ID_text(re_results_list, df):
    Count = 0
    for match1, match2 in zip(re_results_list, re_results_list[1:]):
        # Split on first match and take text after split
        split1 = clean_text_file.split(match1)[1]
        # Split on Second Match and take text before match
        split2 = split1.split(match2)[0]
        # Create key using patent identifier and text as value
        df[match1] = split2
        print(Count)
        Count += 1


create_df_ID_text(re_results_list, df)
df.to_excel('ID_text_table.xlsx')

'''

for match in re_results_list:
    Count +=1
    if Count < 2:
        test1 = clean_text_file[:20000].split(match)[1]
        test2 = test1.split('20030009666')[0]
        
        df[match] = test2


print(df.transpose())
'''

     


