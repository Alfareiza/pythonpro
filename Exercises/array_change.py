def array_change(inputArray: list) -> int:
    """
    You are given an array of integers.
    On each move you are allowed to
    increase exactly one of its element
    by one. Find the minimal number of
    moves required to obtain a strictly
    increasing sequence from the input.
    :param arr:
    :return:
    >>> array_change([1, 1, 1])
    3
    >>> array_change([-1000, 0, -2, 0])
    5
    >>> array_change([2, 1, 10, 1])
    12
    >>> array_change([2, 3, 3, 5, 5, 5, 4, 12, 12, 10, 15])
    13
    """
    target = inputArray[0] - 1
    steps = 0

    for i in inputArray:
        if i > target:
            target = i
        else:
            target = target + 1
            steps += target - i

    return steps
