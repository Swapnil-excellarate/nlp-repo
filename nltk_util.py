import nltk
from nltk.stem import PorterStemmer
stemmer=PorterStemmer()

def tokenized(sentence):
    return nltk.word_tokenize(sentence)

def stem(words):
    return stemmer.stem(words.lower())

def bag_of_word(tokenized_sentence, all_words):
    pass

a= 'Hi how does long shipping take time'
print(a)
a=tokenized(a)
print(a)

stems=[stem(word) for word in a]
print(stems)
