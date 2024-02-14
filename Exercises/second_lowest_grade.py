"""
Given the names and grades for each student in a class
of n students, store them in a nested list and print 
the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest
grade, order their names alphabetically and print each name on 
a new line.

Example
    - [ ["chi", 20.0], ["beta", 50.0], ["alpha", 50.0] ]

The ordered list of scores is [20.0, 50.0], so the second
lowest score is 50.0. There are two students with that score:
["beta", "alpha"]. Ordered alphabetically, the names are printed as:
    - alpha
    - beta
"""

from operator import itemgetter

def solution(names, scores):
    second_lowest = sorted(set(scores))[1]
    for n, s in sorted(zip(names, scores), key=itemgetter(1, 0)):
        if s == second_lowest:
            print(n) 

if __name__ == '__main__':
    scores, names = [], []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names.append(name)
        scores.append(score)
    solution(scores, names)
    
    
