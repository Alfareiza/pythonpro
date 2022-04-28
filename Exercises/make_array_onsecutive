"""
Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, 
each statue having an non-negative integer size. Since he likes to make things perfect, 
he wants to arrange them from smallest to largest so that each statue will be bigger 
than the previous one exactly by 1. He may need some additional statues to be able to 
accomplish that. Help him figure out the minimum number of additional statues needed.

For statues = [6, 2, 3, 8], the output should be
solution(statues) = 3.

Ratiorg needs statues of sizes 4, 5 and 7
"""

def solution(statues: List[int) -> int:
    """
    
    :param statues: List
    :return: int
    >>> solution([6, 2, 3, 8])
    3
    """
    statues = sorted(statues)
    prev_value = statues[0]
    count = 0
    for statue in statues[1:]:
        r = statue - prev_value
        if r > 1:
            count += r-1
        prev_value = statue
    return count
    
if __name__ == '__main__':
    statues = [6, 2, 3, 8]
    print(solution(statues))
    
