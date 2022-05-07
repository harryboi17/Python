import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

para = '''India won the series. Shreyas Iyer is the Man of the Match. Debut match for Avesh'''
sentences = nltk.sent_tokenize(para)
lemm = WordNetLemmatizer()

for i in range(len(sentences)):
  words = nltk.word_tokenize(sentences[i])
  word = [lemm.lemmatize(word) for word in words if word not in set(stopwords.words('english'))]
  sentences[i] = " ".join(word)
  print(sentences[i])