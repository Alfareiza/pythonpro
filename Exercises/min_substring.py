from collections import Counter
from itertools import permutations


def min_window_substring(*str_arr) -> str:
    """
    Consider only two strings, the first parameter being the string N
    and the second parameter being a string K of some characters,
    and your goal is to determine the smallest substring of N that
    contains all the characters in K.
    For example:
        if strArr is ["aaabaaddae", "aed"] then the smallest
        substring of N that contains the characters a, e, and d is "dae"
        located at the end of the string.
        So for this example your program should return the string 'dae'.

    Another example:
        if strArr is ["aabdccdbcacd", "aad"] then the smallest substring
        of N that contains all of the characters in K is "aabd"
        which is located at the beginning of the string. Both parameters
         will be strings ranging in length from 1 to 50 characters and
         all of K's characters will exist somewhere in the string N.
         Both strings will only contains lowercase alphabetic characters.

    :param str_arr:
    :return:
    >>> min_window_substring("aaabaaddae", "aed")
    'dae'
    >>> min_window_substring("aabdccdbcacd", "aad")
    'aabd'
    >>> min_window_substring("ahffaksfajeeubsne", "jefaa")
    'aksfaje'
    >>> min_window_substring("aaffhkksemckelloe", "fhea")
    'affhkkse'
    >>> min_window_substring("aaffsfsfasfasfasfasfasfacasfafe", "fafe")
    'fafe'
    """
    long_str, pattern = str_arr
    result = []

    for permutation in set(permutations(pattern)):
        start = 0
        words_in_permutation = []
        try:
            for letter in permutation:
                try:
                    last_idx = long_str[start:].index(letter)
                except ValueError:
                    raise
                else:
                    end = start + last_idx + 1
                    if not start:
                        words_in_permutation.append(long_str[last_idx:end])
                    else:
                        words_in_permutation.append(long_str[start:end])
                    start = end
            result.append(mount_word(pattern, ''.join(words_in_permutation)))
        except ValueError:
            continue

    return min(result, key=lambda n: len(n))


def mount_word(pattern: str, word: str) -> str:
    counter_pattern = dict(Counter(pattern))
    while 1:
        counter_word = dict(Counter(word))
        if word[0] in counter_pattern and counter_pattern[word[0]] != counter_word[word[0]]:
            word = word[1:]
        else:
            break
    return word


def alternative_min_substring(*strArr):
    long_str, pattern = strArr
    minimum = 100
    substring_counter = Counter(pattern)

    for i, _ in enumerate(long_str):
        for j in range(i + 1, len(long_str) + 1):
            check_counter = Counter(long_str[i:j])
            perfect_match = True
            for key in substring_counter:
                if key not in check_counter:
                    perfect_match = False
                    break
                elif substring_counter[key] > check_counter[key]:
                    perfect_match = False
                    break

            if perfect_match and len(long_str[i:j]) < minimum:
                new_string = long_str[i:j]
                minimum = len(long_str[i:j])

    return new_string

if __name__ == '__main__':
    alternative_min_substring("aaabaaddae", "aed")
