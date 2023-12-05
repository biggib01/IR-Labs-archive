import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer

import timeit
from ordered_set import OrderedSet
import re
import numpy as np
from nltk import PorterStemmer, word_tokenize
from nltk.corpus import stopwords

from cleandata import get_and_clean_data

if __name__ == '__main__':

    results_list = {}
    results_set = {}

    for range_value in range(500, 7001, 500):
        cleaned_description = get_and_clean_data()[:range_value]

        # Replace non-alphabets with spaces and collapse spaces
        cleaned_description = cleaned_description.apply(lambda s: re.sub(r'[^A-Za-z]', ' ', s))
        cleaned_description = cleaned_description.apply(lambda s: re.sub(r'\s+', ' ', s))

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

        # Performance check (time in second)
        XX = X.toarray()

        time_result = round(timeit.timeit(lambda: np.matmul(XX, XX.T), number=1), 3)


        # Save results in list
        results_list.update({ range_value: time_result })

        print(f"Results for range value {range_value}: in List")
        print(f"Time taken: {time_result} seconds")
        print(f"Done.")
        print("---------------------")

        time_result = round(timeit.timeit(lambda: X * X.T, number=1), 3)

        # Save results in set
        results_set.update({ range_value : time_result})

        print(f"Results for range value {range_value}: in Set")
        print(f"Time taken: {time_result} seconds")
        print(f"Done.")
        print("---------------------")

    # Graph time with #samples
    plt.plot(list(results_list.keys()), list(results_list.values()), label='List')
    plt.plot(list(results_set.keys()), list(results_set.values()), label='Set')

    plt.xlabel("#samples")
    plt.ylabel("time in seconds")

    leg = plt.legend(loc='upper center')

    plt.show()

    # Graph times(x) with #samples

    results_listInTimesx = {500: 0}
    results_setInTimesx = {500: 0}

    for range_value in range(1000, 3001, 500):
        results_listInTimesx.update({range_value: int(results_list[range_value] / results_list[500])})
        results_setInTimesx.update({range_value: int(results_set[range_value] / results_set[500])})

    plt.plot(list(results_listInTimesx.keys()), list(results_listInTimesx.values()), label='List')
    plt.plot(list(results_setInTimesx.keys()), list(results_setInTimesx.values()), label='Set')

    plt.xlabel("#samples")
    plt.ylabel("times(x)")

    leg = plt.legend(loc='upper center')

    plt.show()

