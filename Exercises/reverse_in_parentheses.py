def reverse_int_parentheses(s: str) -> str:
    """
    Write a function that reverses characters in (possibly nested)
    parentheses in the input string.

    Input strings will always be well-formed with matching ()s.
    :param input_string:
    :return:
    >>> reverse_int_parentheses("foo(bar(baz))blim")
    "foobazrabblim"
    >>> reverse_int_parentheses("foo(bar)baz(blim)")
    "foorabbazmilb"
    >>> reverse_int_parentheses("foo(bar)baz")
    "foorabbaz"
    >>> reverse_int_parentheses("(bar)")
    "rab"
    """
    end = s.find(")")
    start = s.rfind("(", 0, end)
    if end == -1:
        return s
    return reverse_int_parentheses(s[:start] + s[start + 1:end][::-1] + s[end + 1:])
  
