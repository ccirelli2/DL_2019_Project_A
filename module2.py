# MODULE 2:  FUNCTIONS FOR SCRIPT 2


# Import Libraries

import re
import os
import string
from nltk.stem import *
stemmer = PorterStemmer()
from nltk import corpus
import nltk
import pandas as pd


# Create Text File
def create_concat_txt_file_from_df(df):
    concat_txt_file = open('concat_text.txt', 'w')
    for row in df[0]:
        concat_txt_file.write(str(row))
    print('File Created')

def create_text_file(new_file_name, text_file):
    F = open(new_file_name, 'w')
    F.write(text_file)
    F.close()
    print('{} create'.format(new_file_name))


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
    #Text_strip_nonAlpha = filter(lambda x: x.isalpha(), Text_strip_stopWords)
    # Strip 2 letter words
    Text_strip_2_letter_words = filter(lambda x: len(x)>2, Text_strip_stopWords)
    # Strip names
    Text_strip_names = filter(lambda x: x not in Set_names, Text_strip_2_letter_words)
    # Take Stem of Words
    Text_stem = [stemmer.stem(x) for x in Text_strip_names]
    return list(Text_stem)



# Create Frequency Table
def create_word_freq_table(text):
    
    # Create Dict Object
    Dict = {}

    # Tokenize Text
    tokens = nltk.word_tokenize(text)

    for token in tokens:
        Dict[token] = Dict.get(token, 0) + 1

    df = pd.DataFrame(Dict, index = [0])

    return df.transpose().sort_values(by=[0], ascending = False)










