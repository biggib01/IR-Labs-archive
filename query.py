import pandas as pd
import numpy as np

import cleandata
import parseDB
def query():
    lang = [['java'], ['python'], ['c'], ['kotlin'], ['swift'], ['rust'], ['ruby'], ['scala'], ['julia'],
            ['lua']]
    parsed_description = cleandata.parse_job_description()
    parsed_db = parseDB.parse_db()
    all_terms = lang + parsed_db
    query_map = pd.DataFrame(parsed_description.apply(
        lambda s: [1 if np.all([d in s for d in db]) else 0 for db in all_terms]).values.tolist(),
                             columns=[' '.join(d) for d in all_terms])
    #section 1
    print(query_map)

    #section 2
    print(query_map[query_map['java'] > 0].apply(lambda s: np.where(s == 1)[0],
                                           axis=1).apply(lambda s: list(query_map.columns[s])))