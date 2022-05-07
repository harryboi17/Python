# use pip install nltk if throwing error
import nltk
nltk.download('punkt')
from nltk.stem import PorterStemmer

paragraph = '''HFEKIFGREIFFEDJHFG. WIUGFIWUGFIWUFIUF. UGEDHJWJWEJWEK hey im using whatsapp id786756e75e76ruyhyughjjklklklllk;llkkkjjjiuhuuyuuyyyu  uftyytyuuhjnb  bjnhhjb n hbhggyghh bnghfg'''
Stemmer = PorterStemmer()

sentence = nltk.sent_tokenize(paragraph)
for sent in sentence:
  Stemmer.stem(sent)
  print(sent)

words = nltk.word_tokenize (paragraph)

for word in words:
  Stemmer.stem(word)
  print(word)