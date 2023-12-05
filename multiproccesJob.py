import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer

import timeit
from ordered_set import OrderedSet
import re
import numpy as np
from nltk import PorterStemmer, word_tokenize
from nltk.corpus import stopwords

from cleandata import get_and_clean_data

def function(parsed_description):
    cleaned_description = parsed_description

    # Replace non-alphabets with spaces and collapse spaces
    cleaned_description = cleaned_description.apply(lambda s: re.sub(r'[^A-Za-z]', ' ', str(s)))
    cleaned_description = cleaned_description.apply(lambda s: re.sub(r'\s+', ' ', str(s)))

    # Tokenize
    tokenized_description = cleaned_description.apply(lambda s: word_tokenize(s))

    # Remove stop words
    stop_dict = set(stopwords.words())
    sw_removed_description = tokenized_description.apply(lambda s: list(OrderedSet(s) - stop_dict))
    sw_removed_description = sw_removed_description.apply(lambda s: [word for word in s if len(word) > 2])

    # Create stem caches
    concated = np.unique(np.concatenate([s for s in tokenized_description.values]))
    stem_cache = {}
    ps = PorterStemmer()
    for s in concated:
        stem_cache[s] = ps.stem(s)

    # Stem
    stemmed_description = sw_removed_description.apply(lambda s: [stem_cache[w] for w in s])

    # Vectorize
    cv = CountVectorizer(analyzer=lambda x: x)
    X = cv.fit_transform(stemmed_description)

    XX = X.toarray()

    # print(round(timeit.timeit(lambda: np.matmul(XX, XX.T), number=1), 3))
    print(round(timeit.timeit(lambda: X * X.T, number=1), 3))
