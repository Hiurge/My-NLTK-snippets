import nltk
from nltk import *

my_file = 'Pulpit/nltk_my_snippets/DL_Personality_Detection_from_Text.txt'


# File text into text as variable: 
def file_into_text(my_file):
	a_raw =  open(my_file, "r")
	a_text_raw = a_raw.read()
	return a_text_raw
a_text_raw = file_into_text(my_file) 


# File text into lines list:
def raw_into_text(my_file):
	a_lines = []
	with open(my_file) as file:
		for line in file:
			a_lines.append(line)
	a_text = ""
	for line in a_lines:
		line = line.replace('\n','')
		a_text +=line + " "
	return a_text
a_text = raw_into_text(my_file)


a_words = a_text.split(" ")


# Words that are:
import re
my_text = a_words
longer_than_10_letters = [w for w in my_text if len(w) > 10] 
capitalized = [w for w in my_text if w.istitle()]
starts_with_f = [w for w in my_text if w.startswith('f')]
ends_with_f = [w for w in my_text if w.endswith('f')]
uniqe = set([w.lower() for w in my_text])
regexed_by_at = [w for w in my_text if re.search('@[A-Za-z0-9_]+', w)]


# Frequency of a words:
my_text = a_words
def word_frequency(my_text):
	dist = FreqDist(my_text) # = len(set(my_text))
	dist_keys = dist.keys() # all words
	amount_of_Table_words = dist["Table"] # example
	frequency = [w for w in dist_keys if len(w) > 5 and dist[w] > 15]
	return frequency # Word list that meets criteria
word_frequency = word_frequency(my_text)


# Normalization&stemming - basic word forms
def normalisation_stemming(a_text):
	a_words_norm = a_text.lower().split()
	porter = nltk.PorterStemmer()
	stemmed_words = [porter.stem(t) for t in a_words_norm]
	return stemmed_words
stemmed_words = normalisation_stemming(a_text)


def still_lemmanizer(a_words):
	porter = nltk.stem.porter.PorterStemmer()
	still_lemmatization = [porter.stem(t) for t in a_words[:20]]
	return still_lemmatization
still_lemmatization = still_lemmanizer(a_words)


def lemmanizer(a_words):
	WNlemma = nltk.WordNetLemmatizer()
	s_lemmatization = [WNlemma.lemmatize(t) for t in a_words[:20]]
	return s_lemmatization
lemmatization = still_lemmanizer(a_words)


def tokenizer(a_text):
	tokenized = nltk.word_tokenize(a_text)
	return tokenized
tokenized = tokenizer(a_text)


sentence =  "Merging dataframes become essential when we have information coming from different sources to be collated. Consider a hypothetical case where the average property rates (INR per sq meters) is available for different property types."
def sent_tokenizer(sentence):
	sent_tokenized = nltk.sent_tokenize(text12) # lISTAr 4 ZDAN OSOBNO
	return sent_tokenized
sent_tokenized = sent_tokenizer(sentence)


### POS tagging
# nltk.help.upenn_tagset('MD')

sentence =  "Merging dataframes become essential when we have information coming from different sources to be collated. Consider a hypothetical case where the average property rates (INR per sq meters) is available for different property types."
def pos_taging(sentence):
	sentence = nltk.word_tokenize(sentence)
	pos_tag_sentences = nltk.pos_tag(sentence)
	return pos_tag_sentence
pos_tag_sentence = pos_taging(sentence)


# Parsing sentence structure
sentence = "Alice loves Bob"
def prasing_sent_structure(sentence):
	w_sentence = nltk.word_tokenize(sentence)
	grammar = nltk.CFG.fromstring("""
	S -> NP VP
	VP -> V NP
	NP -> 'Alice' | 'Bob'
	V -> 'loves'
	""")
	parser = nltk.ChartParser(grammar)
	trees = parser.parse_all(w_sentence)
	for tree in trees:
	    print(tree)
	return trees
sent_trees = prasing_sent_structure(sentence)


# Parsing sentence structure
sentence = "I saw the man with a telescope"
def prasing_sent_structure(sentence):
	w_sentence = nltk.word_tokenize() # text = nltk.word_tokenize()
	grammar_1 = nltk.data.load('mygrammar.cfg')
	parser = nltk.ChartParser(grammar1)
	trees = parser.parse_all(text16)
	for tree in trees:
	    print(tree)
	return trees
sent_trees = prasing_sent_structure(sentence)


 
### POS tagging and parsing ambiguity
# from nltk.corpus import treebank
# text17 = treebank.parsed_sents('wsj_0001.mrg')[0]
# print(text17)
