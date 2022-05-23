def two_sum_less_than_number(A: List[int], K: int) -> int:
    """
    Given an array A of integers and integer K, return the maximun S such
    that there exists i < j with A[i] + A[j] = S and S < K. If no such
    i, j exist satisfying this equation return -1
    :param A: List[int] - List of integers
    :param K: int - Upper bound for sum of two numbers in A
    :return: int - Highest sum less than K
    >>> two_sum_less_than_number([34, 23, 1, 24, 75, 33, 54, 8], 60)
    58
    >>> two_sum_less_than_number([10, 20, 30], 15)
    -1
    """
    result = -1
    maximun = K
    A = sorted(A)
    for i in range(len(A) - 1):
        for j in A[i+1:]:
            how_near_is = K - (A[i] + j)
            if 0 < how_near_is < maximun:
                maximun = how_near_is
                result = A[i] + j
            elif how_near_is < 0:
                break

    if result:
        return result
    else:
        return -1
      
