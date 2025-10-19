"""
def solution(n, numlist):
    array = []
    for x in numlist:
            if x%n == 0:
                array.append(x)
    return array
"""

# 리스트 컴프리헨션
def solution(n, numlist):
    return [i for i in numlist if i%n==0]