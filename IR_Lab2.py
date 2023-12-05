import time

from cleandata import parse_job_description
from search import inverse_indexing, search

# Second class
if __name__ == '__main__':
    start_time = time.time()

    parsed_description = parse_job_description()
    invert_idx = inverse_indexing(parsed_description)
    query = 'java oracle'
    matched = search(invert_idx, query)
    print(parsed_description.loc[matched].apply(lambda x: ' '.join(x)).head().to_markdown())
    print("--- %s seconds ---" % (time.time() - start_time))