"""
    Having a json, exclude all the elements within it
    which are in the next list: ['N/A', '-', '']
"""


def clean_data(resp):
    """
    >>> clean_data({'name': {'first': 'Robert', 'middle': '', 'last': 'Smith'}, 'age': 25, 'DOB': '-', 'hobbies': ['running', 'coding'], 'education': {'highschool': 'N/A', 'college': 'Yale'}})
    {'name': {'first': 'Robert', 'last': 'Smith'}, 'age': 25, 'hobbies': ['running', 'coding'], 'education': {'college': 'Yale'}}
    >>> clean_data({'hobbies': ['running', 'coding', '-'], 'education': {'highschool': 'N/A', 'college': 'Yale'} })
    {'hobbies': ['running', 'coding'], 'education': {'college': 'Yale'}}
    """
    return clean_dict(resp)


def clean_dict(dct) -> dict:
    for k in dct.copy():
        value = dct[k]
        if isinstance(value, dict):
            clean_dict(value)
        elif isinstance(value, list):
            clean_list(value)
        else:
            if not value or has_undesirable_values(value):
                del dct[k]
    return dct


def clean_list(lst) -> list:
    for value in lst.copy():
        if isinstance(value, list):
            clean_list(value)
        elif isinstance(value, dict):
            clean_dict(value)
        else:
            if not value or has_undesirable_values(value):
                lst.remove(value)

    return lst


def has_undesirable_values(value):
    undesirables = {'N/A', '-', ''}
    if isinstance(value, int):
        value = f'{value}'.split()
    elif isinstance(value, str):
        value = value.split()

    return bool(undesirables.intersection(value))
