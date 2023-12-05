import parseDB
import cleandata

import numpy as np

def count_python_mysql():
    parsed_description = cleandata.parse_job_description()

    count_python = parsed_description.apply(lambda s: 'python' in s).sum()
    count_1 = parsed_description.apply(lambda s: 'java' in s).sum()
    count_2 = parsed_description.apply(lambda s: 'c' in s).sum()
    count_3 = parsed_description.apply(lambda s: 'kotlin' in s).sum()
    count_4 = parsed_description.apply(lambda s: 'swift' in s).sum()
    count_5 = parsed_description.apply(lambda s: 'rust' in s).sum()
    count_6 = parsed_description.apply(lambda s: 'ruby' in s).sum()
    count_7 = parsed_description.apply(lambda s: 'scala' in s).sum()
    count_8 = parsed_description.apply(lambda s: 'julia' in s).sum()
    count_9 = parsed_description.apply(lambda s: 'lua' in s).sum()


    # add on aws
    count_aws = parsed_description.apply(lambda s: 'aws' in s).sum()
    print('Python: ' + str(count_python) + ' of ' + str(parsed_description.shape[0]))
    print('Java: ' + str(count_1) + ' of ' + str(parsed_description.shape[0]))
    print('C: ' + str(count_2) + ' of ' + str(parsed_description.shape[0]))
    print('Kotlin: ' + str(count_3) + ' of ' + str(parsed_description.shape[0]))
    print('Swift: ' + str(count_4) + ' of ' + str(parsed_description.shape[0]))
    print('Rust: ' + str(count_5) + ' of ' + str(parsed_description.shape[0]))
    print('Ruby: ' + str(count_6) + ' of ' + str(parsed_description.shape[0]))
    print('Scala: ' + str(count_7) + ' of ' + str(parsed_description.shape[0]))
    print('Julia: ' + str(count_8) + ' of ' + str(parsed_description.shape[0]))
    print('Lua: ' + str(count_9) + ' of ' + str(parsed_description.shape[0]))

def count_occurrences():
    cleaned_db = parseDB.parse_db()
    parsed_description = cleandata.parse_job_description()
    raw = [None] * len(cleaned_db)

    #section 1
    for i, db in enumerate(cleaned_db):
        raw[i] = parsed_description.apply(lambda s: np.all([x in s for x in db])).sum()

    #section 2
    with_python = [None] * len(cleaned_db)
    for i, db in enumerate(cleaned_db):
        with_python[i] = parsed_description.apply(lambda s: np.all([x in s for x in db]) and 'python' in s).sum()

    #section 3
    for i, db in enumerate(cleaned_db):
        print(' '.join(db) + ' + python: ' + str(with_python[i]) + ' of ' + str(raw[i]) + ' (' +
              str(np.around(with_python[i] / raw[i] * 100, 2)) + '%)')