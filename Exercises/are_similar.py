def swap_positions(lst: list, start: int, end: int) -> list:
    lst[start], lst[end] = lst[end], lst[start]
    return lst


def are_similar(a: list, b: list) -> bool:
  """
  Are Similar?
  Two arrays are called similar if one can be obtained 
  from another by swapping at most one pair of elements in 
  one of the arrays.

  Given two arrays a and b, check whether they are similar.

  Example
  For a = [1, 2, 3] and b = [1, 2, 3], the output should be
  solution(a, b) = true.

  The arrays are equal, no need to swap any elements.

  For a = [1, 2, 3] and b = [2, 1, 3], the output should be
  solution(a, b) = true.

  We can obtain b from a by swapping 2 and 1 in b.

  For a = [1, 2, 2] and b = [2, 1, 1], the output should be
  solution(a, b) = false.

  Any swap of any two elements either in a or in b won't make a and b equal.
  >>> are_similar([832, 998, 148, 570, 533, 561, 894, 147, 455, 279], 
                  [832, 570, 148, 998, 533, 561, 455, 147, 894, 279])
  False
  >>> are_similar([1, 2, 1, 2, 2, 1], [2, 2, 1, 1, 2, 1])
  True
  """
  if a == b:
      return True
  else:
      idx = 0
      while idx <= len(a) - 1:
          for i in range(1, len(a)):
              if i >= idx:
                  if swap_positions(a.copy(), idx, i) == b:
                      return True
          idx += 1

  return False

# Alternative Solution 1
def solution(a, b):
    same_items = sorted(a) == sorted(b)
    differences = [i for i in range(len(a)) if a[i] != b[i]]
    return len(differences) <= 2 and same_items
  
# Alternative Solution 2
def solution(a, b):
    return sorted(a) == sorted(b) and sum(i!=j for i,j in zip(a,b)) < 3
