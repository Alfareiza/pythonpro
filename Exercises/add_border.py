def adding_border(picture: list) -> list:
    """
    Given a rectangular matrix of characters,
    add a border of asterisks(*) to it.
    Example
    For picture = ["abc",
                   "ded"]
    the output should be :
                         ["*****",
                          "*abc*",
                          "*ded*",
                          "*****"]

    >>> adding_border(["abc", "ded"])
    ['*****', '*abc*', '*ded*', '*****']
    """
    width = max(len(item) for item in picture) + 2
    result = []
    for i in picture:
        len_i = len(i)
        unit_brder = width - len_i
        a = (unit_brder - unit_brder // 2 )* "*" + i + (unit_brder // 2) * "*"
        result.append(a)

    result.insert(0, width * '*')
    result.insert(len(picture)+1, width * '*')
    return result
