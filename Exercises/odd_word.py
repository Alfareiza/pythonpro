
def odd_word(set_one, set_two):
    """
    An odd word is when only appear once and doesn't appear in the other
    iterable.
    >>> odd_word('Junior from Barranquilla is the best', 'Junior from Barranquilla is the greatest')
    ['best', 'greatest']
    >>> odd_word('Facebook Facebook', 'Google')
    ['Google']
    """
    # Create a counter, then filter only unique words and create a set with the result
    unique_words_set_one = set(dict(filter(lambda w: w[1] == 1, Counter(set_one.split()).items())).keys())
    unique_words_set_two = set(dict(filter(lambda w: w[1] == 1, Counter(set_two.split()).items())).keys())
    unique_words_set_one.symmetric_difference(unique_words_set_two)
    return list(unique_words_set_one.symmetric_difference(unique_words_set_two))
