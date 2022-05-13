import panda as pd
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=1500)

corpus = [ 'This is the first document.',
    'This document is the second document.',
    'And this is the third one.',
    'Is this the first document?',]
messages = pd.read_csv('smsspamcollection/SMSSpamCollection',
                           sep='t',names=['labels','message'])

X = cv.fit_transform(corpus).toarray()
y = pd.get_dummies(messages['labels'])

y = y.iloc[:,1].values

from sklearn.model_selection import train_test_split

X_train, y_train, X_test, Y_test = train_test_split(X, y , test_size = 0.2)

from sklearn.naive_bayes import MultinomialNB
model = MultinomialNB()
model.fit(X_train, y_train)
prediction = model.predict(X_test)