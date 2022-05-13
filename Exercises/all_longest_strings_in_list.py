"""
Given an array of strings, return another array containing all of its longest strings.

Example

For input_array = ["aba", "aa", "ad", "vcd", "aba"], the output should be
solution(input_array) = ["aba", "vcd", "aba"].
"""

def all_longest_strings(input_list: list[str]) -> list[str]:
    """
    >>> all_longest_strings(["aba", "aa", "ad", "vcd", "aba"])
    ['aba', 'vcd', 'aba']
    >>> all_longest_strings(["abc", "eeee", "abcd", "dcd"])
    ['eeee', 'abcd']
    >>> all_longest_strings(["ab", "ay", "azd", "abcd", "aaaa", "prtcd"])
    ['prtcd']
    >>> all_longest_strings(["acds", "asdf", "qwerty"])
    ['qwerty']
    """
    new_array, max_len = [], 0
    for i in input:
        if len(i) == max_len:
            max_len = len(i)
            new_array.append(i)
        elif len(i) > max_len:
            max_len = len(i)
            new_array.clear()
            new_array.append(i)
    return new_array
  
  #  Another way of solution
  def all_longest_strings_other_option(input_list):
    return [i for i in input_list if len(i) == len(max(input_list, key=len))]
  
