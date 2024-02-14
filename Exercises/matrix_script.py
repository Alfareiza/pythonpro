"""
Neo has a complex matrix script. The matrix script is a n X m
grid of strings. It consists of alphanumeric characters, 
spaces and symbols (!,@,#,$,%,&).

To decode the script, Neo needs to read each column and 
select only the alphanumeric characters and connect them. 
Neo reads the column from top to bottom and starts reading 
from the leftmost column.
If there are symbols or spaces between two alphanumeric
characters of the decoded script, then Neo replaces them 
with a single space '' for better readability.

Neo feels that there is no need to use 'if' conditions for decoding.

Alphanumeric characters consist of: [A-Z, a-z, and 0-9].
"""
import re

def solution(matrix: list) -> str:
  """
  >>> solution(['Tsi', 'h%x', 'i #', 'sM ', '$a ', '#t%', 'ir!'])
  'This is Matrix#  %!'
  """
  result = [matrix[j][i] for i in range(m) for j in range(n)]
  print(re.sub(r'(?<=[a-zA-Z0-9])[\W\s]+(?=[a-zA-Z0-9])', ' ', ''.join(result)))
  
