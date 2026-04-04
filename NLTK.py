from nltk import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer
from nltk import pos_tag
from nltk import word_tokenize

sent ="Tokenization refers to breakdown the text into smaller units." 
print(word_tokenize(sent))
print(sent_tokenize(sent))


# Create an object of class PorterStemmer
porter = PorterStemmer()
print(porter.stem("playing"))
print(porter.stem("plays"))
print(porter.stem("played"))

# Part Of Speech Tagging
text = "....... is a Computer Science platform."
tokenized_text = word_tokenize(text)
tags = pos_tag(tokenized_text)
print(tags)
