# MODULE 1 - DATA PREPARATION


# Import Modules
import re
import os
import string
from nltk.stem import *
stemmer = PorterStemmer()
from nltk import corpus
import nltk
import pandas as pd



def get_clean_file_utf8(original_file, new_file_name, target_dir):
    # Python throws an error when trying to read text.
    # This code creates a new file and ignores any characters that can't be read.
    
    # Start Function
    print('\n Starting Step 1:  Clean text of non-readable utf8 characters')
    
    # Create New File
    new_file= open(new_file_name, 'w')

    with open(original_file, 'rb') as f:
        lines = [l.decode('utf8', 'ignore') for l in f.readlines()]
        for line in lines:
            new_file.write(line)
        new_file.close()
        print('Finished...\nClean text file written to {}'.format(target_dir), '\n')
    
    return None


def create_df_ID_text(clean_text_file, Excel_file_name, target_dir):
    # Start Function
    print('Starting Step 2:  Creating patent ID and text dataframe...This will take ~ 3 min')

    ## Step1:  Generate List of Patent ID's
    # Create Regex Expression to Find Patent ID's
    regex = re.compile('[0-9]{11}')
    # Get All Matches - Return Iterator
    re_search = re.finditer(regex, clean_text_file)
    # Create DataFrame to Capture Identifer + Text
    df = pd.DataFrame({}, index = [0])
    # Convert Iterator to List
    re_results_list = [x.group() for x in re_search]

    ## Step2:  Form Dataframe
    Count = 0
    for match1, match2 in zip(re_results_list, re_results_list[1:]):
        # Split on first match and take text after split
        split1 = clean_text_file.split(match1)[1]
        # Split on Second Match and take text before match
        split2 = split1.split(match2)[0]
        # Create key using patent identifier and text as value
        df[match1] = split2
        Count += 1

        if Count == 250:
            print('25% Complete')
        elif Count == 500:
            print('50% Complete')
        elif Count == 750:
            print('75% Complete')

    ## Step3:  Write DataFrame to Excel
    df.to_excel(Excel_file_name)
    print('Finished...\nFile {} written to {}'.format(Excel_file_name, target_dir), '\n')

    return None



def load_Patent_ID_table(Patent_ID_file):
    df = pd.read_excel(Patent_ID_file)
    df_transpose = df.transpose()
    return df_transpose


# Create Text File
def create_concat_txt_file_from_df(df, concat_file_name, target_dir):
    print('Starting Step 3:  Create concatenated text file')
    concat_txt_file = open(concat_file_name, 'w')
    for row in df[0]:
        concat_txt_file.write(str(row))
    print('{} written to {}'.format(concat_file_name, target_dir), '\n')

def create_text_file(text_file, new_file_name, target_dir):
    F = open(new_file_name, 'w')
    F.write(text_file)
    F.close()
    print('Finished.  {} written to {}'.format(new_file_name, target_dir), '\n')


def get_set_human_names():
    '''
    Purpose:  obtain a set of all human names
    Input:    none
    Output:   Set of of both female and male names
    '''
    # Create a list of Male names, convert to lower case, split on '\n' 
    # as the text reads in a string as unicode
    Male_names = corpus.names.open('male.txt').read().lower().split('\n')
    # Create a lise of female names, convert to lower case, split on '\n' 
    #as the text reads in a string as unicode
    Female_names = corpus.names.open('female.txt').read().lower().split('\n')
    # Return to the user a set of the concatenation of both lists. 
    return set(Male_names + Female_names)


def clean_and_tokenize_text(Text_file):
    '''
    Input      = Text File
    Operations = Tokenize, lowercase, strip punctuation/stopwords/nonAlpha
    Return     = Object = Set; Set = cleaned, isalpha only tokens
    '''
    
    print('Starting Step 4:  Run dirty text through washer')
    
    # Strip Lists
    Punct_list = set((punct for punct in string.punctuation))
    Stopwords = nltk.corpus.stopwords.words('english')
    Set_names = get_set_human_names()

    # Tokenize Text
    Text_tokenized = nltk.word_tokenize(Text_file)
    # Convert tokens to lowercase
    Text_lowercase = (token.lower() for token in Text_tokenized)

    # Strip Punctuation
    Text_tok_stripPunct = filter(lambda x: (x not in Punct_list), Text_lowercase)
    # Strip Stopwords
    Text_strip_stopWords = filter(lambda x: (x not in Stopwords), Text_tok_stripPunct)
    # Strip Non-Alpha
    Text_strip_nonAlpha = filter(lambda x: x.isalpha(), Text_strip_stopWords)
    # Strip 2 letter words
    Text_strip_2_letter_words = filter(lambda x: len(x)>2, Text_strip_nonAlpha)
    # Strip names
    Text_strip_names = filter(lambda x: x not in Set_names, Text_strip_2_letter_words)
    # Take Stem of Words
    Text_stem = [stemmer.stem(x) for x in Text_strip_names]

    print('Text clean.  Time to dry', '\n')

    return list(set(Text_stem))


# Create Frequency Table
def create_word_freq_table(text, Excel_file_name, target_dir):
    print('Starting Step 5:  Creating word frequency table')

    # Create Dict Object
    Dict = {}

    # Tokenize Text
    tokens = nltk.word_tokenize(text)
    for token in tokens:
        Dict[token] = Dict.get(token, 0) + 1

    # Create Dataframe & Write to File
    df = pd.DataFrame(Dict, index = [0])
    df_t = df.transpose().sort_values(by=[0], ascending = False)
    df_t.to_excel(Excel_file_name)
    print('Finished...\nWord Freq Table File {} written to {}'.format(Excel_file_name, target_dir))

    # Return Table In Memory to User
    return df_t





