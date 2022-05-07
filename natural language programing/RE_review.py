import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

para = '''India won the series. Shreyas Iyer is the Man of the Match. Debut match for Avesh'''

lemm = WordNetLemmatizer()
sent = nltk.sent_tokenize(para)
corpus = []

for i in  range(len(sent)):
  review  = re.sub('[^a-z A-Z]', " ", sent[i])
  review = review.lower()
  review = review.split()

  review = [lemm.lemmatize(word) for word in review if word not in set(stopwords.words('english'))]
  review = " ".join(review)

  corpus.append(review)

for i in range(len(corpus)):
  print(corpus[i])