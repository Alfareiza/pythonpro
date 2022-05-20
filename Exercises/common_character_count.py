def common_character_count(s1: str, s2: str) -> int:
    """
    Given two strings, find the number of common characters between them.
    Example:
        For s1 = "aabcc" and s2 = "adcaa", the output should be:
        solution(s1, s2) = 3.
    Strings have 3 common characters - 2 "a"s and 1 "c"
    :param s1:
    :param s2:
    :return:
    >>> common_character_count('aabcc', 'adcaa')
    3
    >>> common_character_count('a', 'aaa')
    1
    >>> common_character_count('a', 'b')
    0
    >>> common_character_count('abca', 'xyzbac')
    3
    >>> common_character_count('zzzz', 'zzzzzzz')
    4
    """
    count = 0
    commons = set(s1) & set(s2)
    for i in commons:
        count += min(s1.count(i), s2.count(i))
    return count
