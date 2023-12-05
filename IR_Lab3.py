# dense to sparse

from numpy import array
from scipy.sparse import coo_matrix, csr_matrix, csc_matrix, dok_matrix, lil_matrix
import timeit

if __name__ == "__main__" :

    # create dense matrix
    print("-----------------create-----------------")
    A = array([[1, 0, 0, 1, 0, 0], [0, 0, 2, 0, 0, 1], [0, 0, 0, 2, 0, 0]])
    print(A)

    # convert to sparse matrix (COO method)
    print("-----------------convert to sparse matrix (COO method)-----------------")
    S = coo_matrix(A)
    print(S)
    print("-----------------convert COO to CSR-----------------")
    print(S.tocsr()[:,3])

    # reconstruct dense matrix
    print("-----------------reconstruct-----------------")
    B = S.todense()
    print(B)

    times = 100000
    print("-----------------DOK-----------------")
    print(timeit.timeit(lambda : dok_matrix(B), number=times)/times, "sec")
    print("-----------------LIL-----------------")
    print(timeit.timeit(lambda : lil_matrix(B), number=times)/times, "sec")
    print("-----------------CSR-----------------")
    print(timeit.timeit(lambda : csr_matrix(B), number=times)/times, "sec")
    print("-----------------CSC-----------------")
    print(timeit.timeit(lambda : csc_matrix(B), number=times)/times, "sec")