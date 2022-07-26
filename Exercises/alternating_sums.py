def alternating_sums(a: list) -> list
  """
  Several people are standing in a row and need to 
  be divided into two teams. The first person goes
  into team 1, the second goes into team 2, the third 
  goes into team 1 again, the fourth into team 2,
  and so on.

  You are given an array of positive integers - 
  the weights of the people. Return an array of two
  integers, where the first element is the total
  weight of team 1, and the second element is the
  total weight of team 2 after the division is complete.

  Example:
    For a = [50, 60, 60, 45, 70], the output should be
    solution(a) = [180, 105].
    
  >>> alternating_sums([50, 60, 60, 45, 70])
  [180, 105]
"""
    is_odd = lambda x: bool(x % 2)
    group_one, group_two = 0, 0
    for i in range(1, len(a)):
        if is_odd(i):
            group_one += a[i]
        else:
            group_two += a[i]
    group_two += a[0]
    return [group_two, group_one]
    
# Alternative Solution 1
def solution(a):

    return [sum(a[::2]),sum(a[1::2])]

# Alternative Solution 2
def solution(a):
  sums = [0, 0]

  for i, w in enumerate(a):
      sums[i%2] += w

  return sums
