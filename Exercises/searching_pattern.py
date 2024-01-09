"""
Have the function searching_challenge taje str which will be a string
and return the longest pattern within the string. A pattern for this challenge
will be defined as: if at least 2 or more adjacent characteres within the
string repeat at least twice.
So for example "aabecaa" contains the pattern aa, on the other hand "abbbaac"
doesn't contain any pattern. Your program should return "no pattern". So if
str were "123224" the output should return "no null". The string may either
contain all characters (a through z only), integers, or both.
But the parameter will always be a string. Tha mazimum length for the string
being passed in will be 20 characters. If a string for example is "aa2bbbaacbbb"
the pattern is "bbb" and not "aa". You must always return the longest pattern possible.
Examples:
    Input: "da2kr32a2"
    Output: "yes a2"
    Input: "sskfssbbb9bbb"
    Output: "yes bbb"
"""


def searching_challenge(str_param):
    """
    >>> searching_challenge('da2kr32a2')
    'yes a2'
    >>> searching_challenge('sskfssbbb9bbb')
    'yes bbb'
    """
    limit = len(str_param)
    count = 0
    repeated_patterns = set()
    for start, _ in enumerate(str_param):
        for j in range(2, limit):
            count = start + j
            if count > limit:
                break

            pattern = str_param[start:count]
            if str_param.count(pattern, count + 1, limit):
                repeated_patterns.add(pattern)

    if repeated_patterns:
        value = list(repeated_patterns)[-1]
        str_param = f"yes {value}"
    else:
        str_param = 'no pattern'
    return str_param


if __name__ == '__main__':
    print(searching_challenge('da2kr32a2'))
    print(searching_challenge('sskfssbbb9bbb'))
