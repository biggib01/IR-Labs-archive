import multiprocessing.pool
import time
import numpy as np
from matplotlib import pyplot as plt

from cleandata import parse_job_description
from multiproccesJob import function

# Multiprocessing
if __name__ == '__main__':

    results_multiprocess = {}

    for cores in range(1, 9):

        parsed_description = parse_job_description()
        parsed_description_split = np.array_split(parsed_description, cores)

        start_time = time.time()

        with multiprocessing.pool.ThreadPool(cores) as pool:
            pool.map(function, parsed_description_split)
            # result = round(timeit.timeit(lambda: pool.map(function, parsed_description_split)), number=1), 3
            # results_multiprocess.update({ cores : result})

        multi_proc_time = round(time.time() - start_time, 3)

        results_multiprocess.update({cores : multi_proc_time})

        results_multiprocessInTimesx = {1:0}


        print(multi_proc_time)
        print(str(cores) + '-------------------------------')

    for n in range(2, 9):
        results_multiprocessInTimesx.update({n: round(results_multiprocess[1] / results_multiprocess[n], 1)})

    # Graph time with #samples
    plt.plot(list(results_multiprocess.keys()), list(results_multiprocess.values()))

    plt.xlabel("#cores")
    plt.ylabel("time in seconds")

    plt.ylim(0, 30)

    plt.show()

    # Graph times(x) with #samples
    plt.plot(list(results_multiprocessInTimesx.keys()), list(results_multiprocessInTimesx.values()))

    plt.xlabel("#cores")
    plt.ylabel("times(x)")

    plt.show()
