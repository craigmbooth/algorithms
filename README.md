algorithms
==========

Craig's python implementations of various algorithms:

checksum_luhn.py
----------------
Luhn's algorithm for computing a checksum for some decimal data.  As used for e.g. the final digit of credit card numbers.

matrix_multiply_strassen.py
---------------------------
Strassen's recursive algorithm for the multiplication of two matrices.  O(n^2.808).


multiply_recursive_naive.py
---------------------------
A naive recursive algorithm for multiplying two n-digit numbers.  Scales as O(n^2).

multiply_karatsuba.py
---------------------
Optimization of multiply_recursive_naive.py.  O(n^1.55).  Another recursive multiplication algorithm with better scalings.

sort_mergesort_recursive.py
---------------------------
Simple implementation of recursive mergesort algorithm.