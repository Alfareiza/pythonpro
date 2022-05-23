def sort_by_height(a: list[int]) -> list[int]:
    """
    Some people are standing in a row in a park. There are
    trees between them which cannot be moved. Your task is
    to rearrange the people by their heights in a
    non-descending order without moving the trees.
    People can be very tall!
    Example:
        For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
        sort_by_height(a) = [-1, 150, 160, 170, -1, -1, 180, 190].
    :param a: List of integers
    :return: List of sorted integers by height
    >>> sort_by_height([-1, 150, 190, 170, -1, -1, 160, 180])
    [-1, 150, 160, 170, -1, -1, 180, 190]
    >>> sort_by_height([-1, -1, -1, -1, -1])
    [-1, -1, -1, -1, -1]
    >>> sort_by_height([-1])
    [-1]
    >>> sort_by_height([4, 2, 9, 11, 2, 16])
    [2, 2, 4, 9, 11, 16]
    >>> sort_by_height([2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1])
    [1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 2]
    >>> sort_by_height([23, 54, -1, 43, 1, -1, -1, 77, -1, -1, -1, 3])
    [1, 3, -1, 23, 43, -1, -1, 54, -1, -1, -1, 77]
    """
    numbers = sorted(list(filter(lambda n: n >= 0, a)), reverse=True)
    return [-1 if j == -1 else numbers.pop() for k, j in enumerate(a)]
    
