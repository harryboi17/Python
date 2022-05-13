# use pip install nltk if throwing error
import nltk
nltk.download('punkt')
from nltk.stem import PorterStemmer

paragraph = '''Programmers program with programming languages. This is nicest and beautiful place'''
Stemmer = PorterStemmer()

sentence = nltk.sent_tokenize(paragraph)
for sent in sentence:
  print(Stemmer.stem(sent))

words = nltk.word_tokenize (paragraph)

for word in words:
  print(Stemmer.stem(word))
