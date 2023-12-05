import nltk
nltk.download('stopwords')
nltk.download('punkt')
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

#create new variable, contain string.
str1 = 'the chosen software developer will be part of a larger engineering team developing software for medical devices.'
str2 = 'we are seeking a seasoned software developer with strong analytical and technical skills to join our public sector technology consulting team.'

#tokenize means that to remove white space and split the word from paragraph
tokened_str1 = word_tokenize(str1)
tokened_str2 = word_tokenize(str2)

#set true if word have character length more than 2(remove common word phase #1)
tokened_str1 = [w for w in tokened_str1 if len(w) > 2]
tokened_str2 = [w for w in tokened_str2 if len(w) > 2]

#Stop Words: A stop word is a commonly used word (such as “the”, “a”, “an”, “in”) that a search engine has been programmed to ignore, both when indexing entries for searching and when retrieving them as the result of a search query.
#(remove common word phase #2)
no_sw_str1 = [word for word in tokened_str1 if not word in stopwords.words()]
no_sw_str2 = [word for word in tokened_str2 if not word in stopwords.words()]

#Stemming is the process of producing morphological variants of a root/base word. Stemming programs are commonly referred to as stemming algorithms or stemmers.
#(cleaning up word)
ps = PorterStemmer()
stemmed_str1 = np.unique([ps.stem(w) for w in no_sw_str1])
stemmed_str2 = np.unique([ps.stem(w) for w in no_sw_str2])

#sort word [a-z\A-Z]
full_list = np.sort(np.concatenate([stemmed_str1, stemmed_str2]))
