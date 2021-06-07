# -*- coding: utf-8 -*-
"""NLP Assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zmOhJoZv0SdEcQiWYqTWO6ghCCVfQxjs

# NLTK Section

**Importing nltk**
"""

import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

"""**Tokenization**

*Paragraph into sentence*
"""

from nltk.tokenize import sent_tokenize

text = 'This is a sample sentence to check the nltk tools.This is a sentence tokenizer. This will split paragraphs into sentences"

token_text = sent_tokenize(text)
print(token_text)

"""*Sentence into words*"""

text = "This is a sample sentence to check the nltk tools"
token = nltk.word_tokenize(text)
print(token)

"""**POS Tagging**"""

from nltk import pos_tag
text = "This is a sample sentence to check the nltk tools"
t=text.split()
tokens_tag = pos_tag(t)
print(tokens_tag)

"""**Stemming**

*Porter Stemmer*
"""

from nltk.stem import PorterStemmer  
ps = PorterStemmer()



words = ['cared','university','fairly','easily','singing',
       'sings','sung','singer','sportingly'] 
for w in words:
    print(w, " : ", ps.stem(w))

"""*Snowball Stemmer*"""

from nltk.stem.snowball import SnowballStemmer
  
#the stemmer requires a language parameter
snow_stemmer = SnowballStemmer(language='english')
  
#list of tokenized words
words = ['cared','university','fairly','easily','singing',
       'sings','sung','singer','sportingly']

for w in words:
    x = snow_stemmer.stem(w)
    print(w+' : '+x)

"""**N-grams**"""

from nltk.util import ngrams
text = "This is a sample sentence to check the nltk tools"
unigram = ngrams(token,1)
bigrams = ngrams(token,2)
trigrams = ngrams(token,3)
print("Unigram : ")
for i in unigram:
  print(i,end='')
print()
print("Bigram : ")
for i in bigrams:
  print(i,end='')
print()
print("Trigram : ")
for i in trigrams:
  print(i,end='')
print()

"""**Parsing**"""

from nltk.parse import RecursiveDescentParser
grammar = nltk.CFG.fromstring("""  S -> NP VP
  VP -> V NP | V NP PP
  PP -> P NP
  V -> "saw" | "ate" | "walked"
  NP -> "John" | "Mary" | "Bob" | Det N | Det N PP
  Det -> "a" | "an" | "the" | "my"
  N -> "man" | "dog" | "cat" | "telescope" | "park"
  P -> "in" | "on" | "by" | "with"
  """)

rd = RecursiveDescentParser(grammar)
sent = "Mary saw John".split()
for tree in rd.parse(sent):
  print(tree)

"""# Spacy

**Importing spacy**
"""

import spacy
sp = spacy.load('en_core_web_sm')

"""**Tokenization**

*Paragraph into sentence*
"""

document = sp('This is a sample sentence to check the nltk tools.This is a sentence tokenizer.\
 This will split paragraphs into sentences')
for sentence in document.sents:
    print(sentence)

"""*Sentence into words*"""

sentence = sp(u'This is a sample sentence to check the nltk tools')
for word in sentence:
    print(word.text)

"""**POS Tagging**"""

sentence = sp(u'This is a sample sentence to check the nltk tools')
for word in sentence:
    print(word.text, word.pos_)

"""**Lemmatization**"""

sent = sp(u'compute computer computed computing')
for word in sent:
    print(word.text,":",  word.lemma_)

"""**N-grams**"""

sentence = sp(u'This is a sample sentence to check the nltk tool')
for i in sentence.noun_chunks:
  print(i)

"""**Parsing**"""

piano_text = 'Gus is learning piano'
piano_doc = sp(piano_text)
for token in piano_doc:
    print (token.text, token.tag_, token.head.text, token.dep_)