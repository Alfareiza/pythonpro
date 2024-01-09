"""
Have the function array_challenge (str_array) read the str_array parameter being
 passed which will represent the relations among people standing in a line.
 The structure of the input will be ["A>B","B>C","A<D",etc..]. The letters
 stand for different people and the greater than and less than signs stand
 for a person being in front of someone or behind someone. A»B means A is
 in front of B and B<C means that B is behind C in line. For example if
 str_array is: ["J>B","B<S*,D>J], these are the following ways you can
 arrange the people in line: DSJB, SDJB and DJSB. Your program will determine
 the number of ways people can be arranged in line. So for this example
 your program should return the number 3. It also may be the case that the
 relations produce an impossible line ordering, resulting in zero as the answer.
 Only the symbols <, >, and the uppercase letters A...Z will be used.
 The maximum number of relations strarr will contain is ten.
 Example:
     Input:["A>B"，"A<C"，"C<Z"］
     Output: 1
     Input: ["A>B", "B<R", "R<G"]
     Output: 3
"""
from itertools import permutations


def prepare_arr(arr: list) -> list:
    """
    Transform the list which is the input into a list of tuples
    :param arr: Ex.: ["A>B","A<C","C<Z"]
    :return: Ex.: [('A', '>', 'B'), ('A', '<', 'C'), ('C', '<', 'Z')]
    """
    arr_parsed = []
    for i in arr:
        i = i.replace('&#60;', '<')
        arr_parsed.append((i[0], i[1], i[2]))
    return arr_parsed


def detect_letters(arr: list) -> set:
    """
    Detech which letters were received by the program
    :param arr: Ex.: [('A', '>', 'B'), ('A', '<', 'C'), ('C', '<', 'Z')]
    :return: Ex.: {'A', 'B', 'C', 'Z'}
    """
    letters = set()
    for letter in arr:
        letters.add(letter[0])
        letters.add(letter[2])
    return letters


def create_rules(arr_parsed: list, letters: set) -> dict:
    """
    Create a dict which map all the letters and their corresponds
     when they are high o less than the main letter.
    :param arr_parsed: Ex.: [('A', '>', 'B'), ('A', '<', 'C'), ('C', '<', 'Z')]
    :param letters: Ex.: {'A', 'B', 'C', 'Z'}
    :return: Ex.: {
                    'A': {'<': ['C'], '>': ['B']},
                    'B': {'<': ['A'], '>': []},
                    'C': {'<': ['Z'], '>': ['A']},
                    'Z': {'<': [], '>': ['C']}
                }
    """
    refs = {letter: {'<': [], '>': []} for letter in letters}
    opposite = {'>': '<', '<': '>'}

    for w in arr_parsed:
        left, than, right = w
        refs[left][than].append(right)
        new_than = opposite[than]
        refs[right][new_than].append(left)

    return refs


def order_is_ok(refs: dict, combinations: tuple) -> bool:
    """ Determine if the combination of letters match with the logic
    of the str_array according to the greater than and less than signs."""
    for idx, letter in enumerate(combinations):
        for x in refs[letter]['<']:
            if not combinations.index(x) < idx:
                return False

        for x in refs[letter]['>']:
            if combinations.index(x) < idx:
                return False

    return True


def array_challenge(str_arr):
    """
    Main function responsible for solve the array challenge
    >>> array_challenge(["A>B","A<C","C<Z"])
    1
    >>> array_challenge(["A>B", "B<R", "R<G"])
    3
    """
    str_array_parsed = prepare_arr(str_arr)

    if not str_array_parsed:
        return 0

    letters = detect_letters(str_array_parsed)
    refs = create_rules(str_array_parsed, letters)

    count = 0
    for combination in permutations(letters):
        if order_is_ok(refs, combination):
            count += 1

    return count
