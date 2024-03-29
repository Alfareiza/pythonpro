"""
After becoming famous, the CodeBots decided to move into a new building together.
Each of the rooms has a different cost, and some of them are free, but there's a
rumour that all the free rooms are haunted! Since the CodeBots are quite superstitious, 
they refuse to stay in any of the free rooms, or any of the rooms below any of the free rooms.

Given matrix, a rectangular matrix of integers, where each value represents the cost of the 
room, your task is to return the total sum of all rooms that are suitable for the CodeBots
(ie: add up all the values that don't appear below a 0).

For:
  matrix = [[0, 1, 1, 2], 
            [0, 5, 0, 0], 
            [2, 0, 3, 3]]
The output should be 9.

Here are several haunted rooms, so we'll disregard them as well as any rooms beneath them.
Thus, the answer is 1 + 5 + 1 + 2 = 9

For

matrix = [[1, 1, 1, 0], 
          [0, 5, 0, 1], 
          [2, 1, 3, 10]]
The output should be 9.

Note that the free room in the final column makes the full column unsuitable for 
bots (not just the room directly beneath it). 
Thus, the answer is 1 + 1 + 1 + 5 + 1 = 9.
"""
def matrix_elements_sum(matrix: list[list[int]]) -> int:
    """
    >>>  matrix_elements_sum([[0, 1, 1, 2],
    ...                      [0, 5, 0, 0],
    ...                      [2, 0, 3, 3]])
    9
    >>>  matrix_elements_sum([[1, 1, 1, 0],
    ...                       [0, 5, 0, 1],
    ...                       [2, 1, 3, 10]])
    9
    >>>> matrix_elements_sum([[1, 2, 3, 4, 5]])
    15
    >>> matrix_elements_sum([[4, 0, 1], 
    ...                      [10, 7, 0], 
    ...                      [0, 0, 0], 
    ...                      [9, 1, 2]])
    15
    """
    invalid_columns = []
    result = 0
    for rows in matrix:
        for j, value in enumerate(rows):
            if j in invalid_columns:
                continue
            elif value == 0:
                invalid_columns.append(j)
            else:
                result += value
    return result
  
  
# Another way of solution
def matrix_elements_sum_(matrix):
    # Ex.: Matrix:
    #              [[0, 1, 1, 2],
    #               [0, 5, 0, 0],
    #               [2, 0, 3, 3]]
    # 
    m = list(zip(*matrix))
    # Ex.: m:
    #              [[0, 0, 2], [1, 5, 2], [1, 0, 3], [2, 0, 3]]
    sum = 0
    for l in m:
        for n in l:
            if n == 0:
                break
            else:
                sum += n         
    return sum
