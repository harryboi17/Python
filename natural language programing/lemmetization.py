import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.stem import WordNetLemmatizer

para = '''Hello, Harshit Bansal here what you doin'? or i must say How you doing finally historical children coming chips?'''
para2 = '''apples dictonary universities children chips'''
words = nltk.word_tokenize(para2)

lemm = WordNetLemmatizer()
for word in words:
  print(lemm.lemmatize(word))