import nltk 
import pandas as pd 
import numpy as np 
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords 


nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

dataframe = pd.read_csv('spam.csv', encoding = 'latin-1')
dataframe = dataframe.drop(["Unnamed: 2", "Unnamed: 3", "Unnamed: 4"], axis = 1)
dataframe = dataframe.rename(columns={'v1': 'label', 'v2': 'msg'})

dataframe['msg'] = dataframe['msg'].str.lower()
dataframe['msg'] = dataframe['msg'].apply(word_tokenize)

def remove_stop_words(tokens):
    stopwrds = set(stopwords.words('english'))
    filtered = [word for word in tokens if word not in stopwrds]
    return filtered

def concatenate_words(tokens):
    concat = ' '.join(tokens)
    return concat

dataframe['msg'] = dataframe['msg'].apply(remove_stop_words)
dataframe['msg'] = dataframe['msg'].apply(concatenate_words)

print(dataframe['msg'])

