def count_substring_occurrences(a, b) -> int:
    """
    Given a sentence a and a word b, we want to find the maximum
    number of times the word b is repeated in a.
    The repeated words should be concatenated and placed
    next to each other.
    According to the next example the result should be 2, because
    "po" is twice, one at the end of the string A and another one
    which is concatenated with "po" + "po" at the beginning of
    the string A.
    >>> solution("popokpo", "po")
    2
    """
    ref = []
    for i in range(len(a) - len(b) + 1):
        if a[i:i + len(b)] == b:
            if not ref:
                # Get into here when ref is empty
                ref.append(i)
            elif abs(ref[-1] - i) > len(b):
                # Get into here when diff is higher than b string
                ref.append(i)

    return len(ref)
