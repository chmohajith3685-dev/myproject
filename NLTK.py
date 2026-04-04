import nltk
 
# Download required datasets (run only once)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
 
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import pos_tag
 
text = "Natural Language Processing is amazing. NLTK makes text processing easy in Python!"
 
# --- 1. Sentence Tokenization ---
sentences = sent_tokenize(text)
print("Sentences:", sentences)
 
# --- 2. Word Tokenization ---
words = word_tokenize(text)
print("\nWords:", words)
 
# --- 3. Remove Stopwords ---
stop_words = set(stopwords.words('english'))
filtered = [w for w in words if w.lower() not in stop_words]
print("\nAfter Stopword Removal:", filtered)
 
# --- 4. Stemming ---
stemmer = PorterStemmer()
stemmed = [stemmer.stem(w) for w in filtered]
print("\nStemmed Words:", stemmed)
 
# --- 5. Lemmatization ---
lemmatizer = WordNetLemmatizer()
lemmatized = [lemmatizer.lemmatize(w) for w in filtered]
print("\nLemmatized Words:", lemmatized)
 
# --- 6. POS Tagging ---
pos_tags = pos_tag(words)
print("\nPOS Tags:", pos_tags)
 
