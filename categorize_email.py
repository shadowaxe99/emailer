from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from nltk.tokenize import word_tokenize
import pandas as pd

# Assume we have a pandas DataFrame `emails`
# with columns 'text' (contains email body) and 'label' (the category of the email)

# Prepare the BOW (bag of words) transformer using CountVectorizer
vectorizer = CountVectorizer(tokenizer=word_tokenize, stop_words='english')
X = vectorizer.fit_transform(emails['text'])

# Train the Naive Bayes classifier
clf = MultinomialNB()
clf.fit(X, emails['label'])

def categorize_email(email_text):
    email_bow = vectorizer.transform([email_text])
    return clf.predict(email_bow)[0]

# Usage:
# email_category = categorize_email('This is the body of the email')