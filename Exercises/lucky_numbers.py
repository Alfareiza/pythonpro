def first_part_equal_to_second_part(number: int) -> bool:
    """
    Ticket numbers usually consist of an even number of digits.
    A ticket number is considered lucky if the sum of the first half
    of the digits is equal to the sum of the second half.

    Given a ticket number n, determine if it's lucky or not.

    Example:
        For number = 1230, the output should be
        first_part_equal_to_second_part(number) = true;
        For number = 239017, the output should be
        first_part_equal_to_second_part(number) = false.

    :param number:
    :return: True or False
    >>> first_part_equal_to_second_part(239017)
    False
    >>> first_part_equal_to_second_part(1230)
    True
    >>> first_part_equal_to_second_part(111222)
    False
    """
    number = str(number)
    if len(number) % 2 == 0 and \
            sum(list(map(int, number[:len(number) // 2]))) == \
            sum(list(map(int, number[len(number) // 2:]))):
        return True
    else:
        return False
