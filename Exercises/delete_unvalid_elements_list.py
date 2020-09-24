def delete_unvalid_terms(unvalid_terms: list, the_list: list):
    """
    Receive two lists
    unvalid_terms: this list contain the terms that you dont want in list2
    the_list: Delete all the unvalid terms of this list.
    Return: new_list: New list without unvalid terms.
    """
    new_list = [i for i in the_list if i not in unvalid_terms]
    return new_list


if __name__ == '__main__':
    terms = [0, '0', False, None]
    values = ['alfonso', 1, False, 'celular', None, 0, '0', 'junior']
    print(delete_unvalid_terms(terms, values))
