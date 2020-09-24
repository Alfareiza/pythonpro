def planar_array(the_list: list):
    """
    Receive a list that coud have list inside (some levels).
    Ex. : the_list = [[1, 2], [3, 4], [5, 6], 3, 4 ]
    Return new_list = [1, 2, 3, 4, 5, 6, 3, 4]
    """
    new_list = []
    for items in the_list:
        if isinstance(items, list):
            for i in items:
                new_list.append(i)
        else:
            new_list.append(items)

    return new_list


if __name__ == '__main__':
    arr = [[1, 2], [3, 4], [5, 6], 3, 4]
    print(planar_array(arr))
