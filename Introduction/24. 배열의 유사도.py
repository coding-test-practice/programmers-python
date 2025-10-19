"""
def solution(s1, s2):
    count = 0
    for x in s1:
        for y in s2:
            if x==y:
                count += 1
    return count
"""

def solution(s1, s2):
    count = 0
    for x in s1:
        if x in s2:
            count += 1
    return count