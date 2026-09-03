import nltk 
import pandas as pd 
import numpy as np 

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords 
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report, accuracy_score 
from sklearn.naive_bayes import MultinomialNB


nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')


# READING DATASET INTO A 2-D PANDAS DATAFRAME 
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


# APPLYING FUNCTIONS TO THE MSG COLUMN TO REMOVE STOP WORDS FROM EACH ROW AND CONCATENATE THE LIST
dataframe['msg'] = dataframe['msg'].apply(remove_stop_words)
dataframe['msg'] = dataframe['msg'].apply(concatenate_words)


# SPLITING THE SAMPLES FOR TRAINING AND EVENTUAL TESTING
X_train_text, X_test_text, y_train, y_test = train_test_split(
    dataframe['msg'], 
    dataframe['label'], 
    test_size = 0.25, 
    random_state = 26
)


# CREATING AN INSTANCE OF COUNTVECTOSRIZER TO LEARN AND TRANSFORM TRAINING AND TEST SAMPLES
vectorizer = CountVectorizer()

X_train = vectorizer.fit_transform(X_train_text)
X_test = vectorizer.transform(X_test_text)

clf = MultinomialNB()
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, output_dict=True)

print(f'{accuracy * 100}%')
print(classification_report(y_test, y_pred))


# TESTING THE MODEL WITH A CUSTOM EMAIL MESSAGE 

def preprocess_message(message):
    tokens = word_tokenize(message.lower())
    return concatenate_words(remove_stop_words(tokens))

def predict_message(message):
    processed_message = preprocess_message(message)
    message_vector = vectorizer.transform([processed_message])
    prediction = clf.predict(message_vector)[0]
    confidence = clf.predict_proba(message_vector).max()
    return prediction, confidence

while True:
    message = input("\nPaste an email to classify, or press Enter to quit: ").strip()
    if not message:
        break

    prediction, confidence = predict_message(message)
    print(f"Prediction: {prediction} ({confidence:.1%} confidence)")

"""

Classification Report:
              precision    recall  f1-score   support

        ham       0.99      0.99      0.99      1213
        spam       0.94      0.93      0.94       180

        accuracy                           0.98      1393
        macro avg       0.96      0.96      0.96      1393
        weighted avg       0.98      0.98      0.98      1393

"""