def solution(array, n):
    count = 0
    for x in array:
        if x == n:
            count += 1
    return count